import os

import pygame
from requests import get

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode=Австралия&format=json"
response = get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']
    ll = toponym['Point']['pos'].replace(' ', ',')
    f_1, f_2 = map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split())
    s_1, s_2 = map(float, toponym['boundedBy']['Envelope']['upperCorner'].split())
    spn = ','.join([str(s_1 - f_1), str(s_2 - f_2)])
    photo = get(f'https://static-maps.yandex.ru/1.x/?ll={ll}8&spn={spn}&l=sat')

    map_file = "maps.jpg"
    try:
        with open(map_file, "wb") as file:
            file.write(photo.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        exit(2)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    while pygame.event.wait().type != pygame.QUIT:
        clock.tick(30)
    pygame.quit()

    os.remove(map_file)
