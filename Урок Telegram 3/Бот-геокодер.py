import telebot
from get_spn import get_spn
from requests import get

bot = telebot.TeleBot("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")


@bot.message_handler(func=lambda m: True)
def geocoder(message):
    geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
    response = get(geocoder_uri, params={
        "format": "json",
        "geocode": message.text
    })

    if response.status_code != 200:
        bot.send_message(message.chat.id, 'Ошибка ' + str(response.status_code))
        return
    toponym = response.json()["response"]["GeoObjectCollection"]
    if toponym['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
        bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')
        return
    toponym = toponym["featureMember"][0]["GeoObject"]

    ll = toponym['Point']['pos'].replace(' ', ',')
    spn = get_spn(toponym)

    static_api_request = \
        f"http://static-maps.yandex.ru/1.x/?spn={spn}&l=sat&pt={ll},flag"

    bot.send_photo(
        message.chat.id,  # Идентификатор чата.
        # Куда посылать картинку.
        # Ссылка на static API, по сути, ссылка на картинку.
        static_api_request
    )
    # Телеграму можно передать прямо её, не скачивая предварительно карту.


bot.polling()
