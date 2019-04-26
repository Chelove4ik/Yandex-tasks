from time import sleep

import telebot

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')


@bot.message_handler(commands=['set_timer'])
def close(message):
    time = int(message.text.split()[1])
    bot.send_message(message.from_user.id, f'Вернусь через {time} секунд')
    sleep(time)

    bot.send_message(message.from_user.id, 'Я тутачки')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.from_user.id, message.text[::-1])


bot.polling()
