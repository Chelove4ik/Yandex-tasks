from pprint import pprint

import requests


def okrug(name):
    try:
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?geocode={name}&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]['metaDataProperty'][
                'GeocoderMetaData']['Address']['Components'][1]['name']
            pprint(toponym)
    except:
        print("Запрос не удалось выполнить. Проверьте подключение к сети Интернет.")


lst = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']
for nm in lst:
    okrug(nm)
