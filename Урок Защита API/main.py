import os

import telebot
from APIs import Musixmatch, gtts
from auth import telegram_api_key, musixmatch_api_key
from telebot import types

bot = telebot.TeleBot(telegram_api_key)
musixmatch = Musixmatch(musixmatch_api_key)


@bot.message_handler(commands=['start'])
def handle_time(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/help')
    markup.add('/close')
    bot.send_message(message.from_user.id, 'Приветствую тебя', reply_markup=markup)
    help(message)


@bot.message_handler(commands=['close'])
def close(message):
    bot.send_message(message.from_user.id, 'Пока. Если захочешь продолжить, пиши /start',
                     reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, '''Если хотите найти текст песни, то введите всё что Вы заете о песне: автор, название, запомнившейся текст
    Если хотите озвучить текст песни с помощью гугл девушки, то напишите /read_lyrics и всё что знаете о песне''')


@bot.message_handler(commands=['read_lyrics'])
def read_lyrics(message):
    try:
        info = message.text[12::]
        print(info)
        user_id = message.from_user.id
        data = musixmatch.get_lyrics(info)['message']['body']['lyrics']['lyrics_body']
        gtts(data, 'ru', user_id)
        file = open(f'{user_id}.mp3', 'rb')
        bot.send_voice(user_id, file)
        file.close()
        os.remove(f'{user_id}.mp3')
    except Exception as ex:
        print(ex)


@bot.message_handler(commands=['get_lyrics'])
def get_lyrics(message):
    try:
        info = message.text[11::]
        data = musixmatch.get_lyrics(info)['message']['body']['lyrics']['lyrics_body']
        bot.send_message(message.from_user.id, data)
    except Exception:
        bot.send_message(message.from_user.id, 'Текст для песни не найден или такой песни не существует')


bot.polling()
