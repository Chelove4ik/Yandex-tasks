import os

import pygame
from requests import get


def get_coords(name):
    request = f"http://geocode-maps.yandex.ru/1.x/?geocode={name}&format=json"
    info = get(request).json()["response"]["GeoObjectCollection"]["featureMember"][0][
        "GeoObject"]['Point']['pos'].replace(' ', ',')
    return info


geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode=Москва&format=json"
response = get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']
    ll = toponym['Point']['pos'].replace(' ', ',')
    spn = '0.1,0.1'
    points = '~'.join([get_coords(i) for i in ['Москва, Спартак', 'Динамо', 'Лужники']])
    photo = get(f'https://static-maps.yandex.ru/1.x/?ll={ll}8&spn={spn}&l=map&pt={points}')

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
