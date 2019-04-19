import os

import pygame
from requests import get

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode=Финский залив, Санкт-Петербург&format=json"
response = get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']
    ll = toponym['Point']['pos'].replace(' ', ',')
    spn = '0.12,0.19'
    pl = '29.909184,59.885118,29.912919,59.891245,30.206151,59.919913,30.258248,59.917525,30.267206,59.919417,30.275123,59.931089,30.310724,59.941660,30.312958,59.940869'

    photo = get(f'https://static-maps.yandex.ru/1.x/?l=map&pl={pl}&spn={spn}')

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
