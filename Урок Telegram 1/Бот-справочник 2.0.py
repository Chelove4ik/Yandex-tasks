import telebot
from telebot import types

bot = telebot.TeleBot("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")


@bot.message_handler(commands=['address'])
def address(message):
    bot.send_message(message.from_user.id, 'Адрес: г. Москва, ул. Льва Толстого, 16')


@bot.message_handler(commands=['phone'])
def phone(message):
    bot.send_message(message.from_user.id, 'Телефон: +7(495)776-3030')


@bot.message_handler(commands=['site'])
def site(message):
    bot.send_message(message.from_user.id, 'Сайт: http://www.yandex.ru/company')


@bot.message_handler(commands=['work_time'])
def site(message):
    bot.send_message(message.from_user.id, 'Время работы: пн-пт -- 9-00 - 19-00')


@bot.message_handler(commands=['close'])
def close(message):
    bot.send_message(message.from_user.id, 'closed', reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['start'])
def handle_time(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/address', '/phone')
    markup.add('/site', '/work_time')
    markup.add('/close')
    bot.reply_to(message, 'Welcome', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Я получил сообщение ' + message.text)


bot.polling(none_stop=True, interval=0)
