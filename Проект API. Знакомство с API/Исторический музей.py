import requests

zapros = 'Исторический музей, город Москва, Красная пл-дь, 1'

geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?geocode={zapros}&format=json"

response = None

try:
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_coodrinates = toponym["Point"]["pos"]
        print(toponym_address, "имеет координаты:", toponym_coodrinates)
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
except:
    print("Запрос не удалось выполнить. Проверьте подключение к сети Интернет.")
