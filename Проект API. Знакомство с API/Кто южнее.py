from sys import argv

from requests import get

argv = argv[1::]


def get_coords(name):
    request = f"http://geocode-maps.yandex.ru/1.x/?geocode={name}&format=json"
    info = get(request).json()["response"]["GeoObjectCollection"]["featureMember"][0][
        "GeoObject"]['Point']['pos'].split()[1]
    return info


lst = []
for i in argv:
    lst.append(float(get_coords(i)))

print(argv[lst.index(min(lst))])
