import os
from sys import argv

import pygame
import requests
from distance import lonlat_distance

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

# address_ll = '37.6222,55.7566'
address_ll = ','.join(argv[1::])

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    # ...
    pass

# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]

# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "l": "map",
    "pt": "{0},pm2dgl~{1},pm2grm".format(org_point, address_ll)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

map_file = "maps.jpg"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    exit(2)

pygame.init()
screen = pygame.display.set_mode((1000, 450))
screen.blit(pygame.image.load(map_file), (0, 0))

myfont = pygame.font.SysFont('arial', 15)

addr = myfont.render(''.join(org_address), 1, (255, 255, 255))
name = myfont.render(organization['properties']['CompanyMetaData']['name'], 1, (255, 255, 255))
time = myfont.render(organization['properties']['CompanyMetaData']['Hours']['text'], 1, (255, 255, 255))
distance = myfont.render(str(int(lonlat_distance((address_ll.split(',')), point))) + ' метров', 1, (255, 255, 255))

screen.blit(addr, (610, 0))
screen.blit(name, (610, 20))
screen.blit(time, (610, 40))
screen.blit(distance, (610, 60))

pygame.display.flip()
clock = pygame.time.Clock()
while pygame.event.wait().type != pygame.QUIT:
    clock.tick(30)
pygame.quit()

os.remove(map_file)
