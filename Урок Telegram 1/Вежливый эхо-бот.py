import logging

import telebot

bot = telebot.TeleBot("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(name)s %(message)s')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.from_user.id, 'Я получил сообщение ' + message.text)


bot.polling()
