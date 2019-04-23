import os
from sys import argv

import pygame
import requests


def kruglosutochno(data):
    try:
        if data['properties']['CompanyMetaData']['Hours']['Availabilities'][0]['TwentyFourHours']:
            return True
    except:
        return False


map_file = "maps.jpg"

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {"geocode": toponym_to_find, "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
coords = ','.join(toponym_coodrinates.split())

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = coords

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz",
}

response = requests.get(search_api_server, params=search_params)

json_response = response.json()

organizations = json_response["features"][:10]
delta = '0.03'
pharmacies_points = []

for org in organizations:
    point = org["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    twfo = kruglosutochno(org)
    pharmacies_points.append(org_point + ',pm2dgl~' if twfo else org_point + ',pm2bll~')

pharmacies_points[-1] = pharmacies_points[-1][:-1]

map_params = {
    "l": "sat",
    "pt": f"{''.join([p for p in pharmacies_points])}"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

with open(map_file, mode='wb') as f:
    f.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))

img = pygame.image.load(map_file)
screen.blit(img, (0, 0))

pygame.display.flip()
clock = pygame.time.Clock()
while pygame.event.wait().type != pygame.QUIT:
    clock.tick(30)
pygame.quit()

os.remove(map_file)
