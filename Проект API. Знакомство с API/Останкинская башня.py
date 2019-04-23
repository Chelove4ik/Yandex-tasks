from sys import argv

import requests
from distance import lonlat_distance


def coords_by_addr(addr, formatted=False):
    response = requests.get(
        f'http://geocode-maps.yandex.ru/1.x/?geocode={addr}&format=json').json()[
        'response']['GeoObjectCollection']['featureMember']
    coords = list(map(float, response[0]['GeoObject']['Point']['pos'].split()))
    if formatted:
        coords = ','.join(list(map(str, coords)))
    return coords


addr = ' '.join(argv[1:]).split(';')
home_f = coords_by_addr(addr[0], True)
school_f = coords_by_addr(addr[1], True)
home = coords_by_addr(addr[0])
school = coords_by_addr(addr[1])

l = int(lonlat_distance(home, school))
h1 = 525
h2 = (l / 3.6 - h1 ** 0.5) ** 2
print(int(h2))
