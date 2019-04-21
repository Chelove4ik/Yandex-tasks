from sys import argv
from requests import get

coords = ','.join(argv[1::])

metro = get(f'https://geocode-maps.yandex.ru/1.x/?geocode={coords}&kind=metro&sco=latlong&format=json').json()[
    'response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
print(metro['description'], metro['Point']['pos'], sep='\n')
