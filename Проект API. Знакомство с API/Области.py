import requests


def okrug(name):
    try:
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?geocode={name}&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]['metaDataProperty'][
                'GeocoderMetaData']['Address']['Components'][2]['name']
            print(toponym)
    except:
        print("Запрос не удалось выполнить. Проверьте подключение к сети Интернет.")


lst = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']
for nm in lst:
    okrug(nm)
