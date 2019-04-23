from sys import argv

from requests import get

geo_api_server = "http://geocode-maps.yandex.ru/1.x/"

print(' '.join(argv[1::]))

search_params = {
    "geocode": ' '.join(argv[1::]),

    "format": "json"
}

response = \
    get(geo_api_server, params=search_params).json()['response']['GeoObjectCollection'][
        'featureMember'][0]['GeoObject']['Point']['pos'].replace(' ', ',')

params_district = {
    "geocode": response,
    'kind': 'district',
    "format": "json"
}

answer = get(geo_api_server, params=params_district).json()

print(answer['response']['GeoObjectCollection'][
          'featureMember'][0]['GeoObject']['metaDataProperty'][
          'GeocoderMetaData']['Address']['Components'][-1]['name'])
