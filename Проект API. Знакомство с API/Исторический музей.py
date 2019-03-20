import requests

response = requests.get(
    "http://geocode-maps.yandex.ru/1.x/?geocode=Исторический музей, Москва, Красная площадь, 1)&format=json").json()[
    'response']['GeoObjectCollection']['featureMember']

for i in response:
    i = i['GeoObject']
    if 'Москва' in i['description'] and \
            'Красная площадь, 1' in i['metaDataProperty']['GeocoderMetaData']['Address']['formatted']:
        print('адрес:', i['metaDataProperty']['GeocoderMetaData']['Address']['formatted'])
        print('координаты:', i['Point']['pos'])
