import logging

import telebot
from requests import get
from telebot import types

bot = telebot.TeleBot("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(name)s %(message)s')

sessionStorage = {}


@bot.message_handler(commands=['start'])
def handle_time(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/ru', '/en')
    bot.send_message(message.from_user.id, 'Приветствую тебя', reply_markup=markup)


@bot.message_handler(commands=['ru', 'en'])
def change_lang(message):
    sessionStorage[message.from_user.id] = 'ru' if message.text == '/ru' else 'en'


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    try:
        bot.send_message(message.from_user.id, translate(message.text, sessionStorage[message.from_user.id]))
    except Exception:
        bot.send_message(message.from_user.id, 'Что-то пошло не так')


def translate(text, lan):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    param = {
        'key': 'trnsl.1.1.20190427T100302Z.81d7d299b06261b2.9452dc6a4d8aae7dc4e0980fdf76cd383858c21f',
        'text': text,
        'lang': lan
    }
    return get(url, param).json()['text'][0]


bot.polling()
