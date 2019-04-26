import logging
from time import asctime

import telebot

bot = telebot.TeleBot("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(name)s %(message)s')


@bot.message_handler(commands=['time'])
def time(message):
    bot.send_message(message.from_user.id, asctime()[10:19])


@bot.message_handler(commands=['date'])
def date(message):
    bot.send_message(message.from_user.id, asctime()[:10])


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.from_user.id, message.text[::-1])


bot.polling()
