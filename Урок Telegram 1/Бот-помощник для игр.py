import time
from multiprocessing import Process
from random import randint

import telebot
from telebot import types

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')
chat_id = None


@bot.message_handler(commands=['hexagonal'])
def hex(message):
    bot.send_message(message.from_user.id, str(randint(1, 6)))


@bot.message_handler(commands=['hexagonal_2'])
def hex_2(message):
    bot.send_message(message.from_user.id, str(randint(1, 6)) + ' ' + str(randint(1, 6)))


@bot.message_handler(commands=['twenty_sided'])
def twenty(message):
    bot.send_message(message.from_user.id, str(randint(1, 20)))


@bot.message_handler(commands=['come_back'])
def back(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/dice', '/timer')
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=markup)


@bot.message_handler(commands=['set_timer'])
def close(message):
    global p1
    try:
        if message.text[-1] == 'm':
            x = int(message.text.split()[1][:-1]) * 60
        else:
            x = int(message.text.split()[1][:-1])
        p1 = Process(target=start_timer, args=(x,))
        p1.start()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
        markup.add('/close')
        bot.send_message(message.from_user.id, 'Таймер запущен', reply_markup=markup)
    except ValueError:
        return


@bot.message_handler(commands=['close'])
def twenty(message):
    global p1
    p1.terminate()
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/set_timer 30s', '/set_timer 1m')
    markup.add('/set_timer 5m', '/come_back')
    bot.send_message(chat_id, 'Таймер остановлен', reply_markup=markup)


@bot.message_handler(commands=['dice'])
def handle_dice(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/hexagonal', '/hexagonal_2')
    markup.add('/twenty_sided', '/come_back')
    bot.send_message(chat_id, 'Выберите', reply_markup=markup)


@bot.message_handler(commands=['timer'])
def handle_timer(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/set_timer 30s', '/set_timer 1m')
    markup.add('/set_timer 5m', '/come_back')
    bot.send_message(chat_id, 'Выберите', reply_markup=markup)


@bot.message_handler(commands=['start'])
def handle_start(message):
    global chat_id
    chat_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/dice', '/timer')
    bot.send_message(chat_id, 'Добро пожаловать', reply_markup=markup)


def start_timer(n):
    global chat_id
    time.sleep(n)
    print(n)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/set_timer 30s', '/set_timer 1m')
    markup.add('/set_timer 5m', '/come_back')
    bot.send_message(chat_id, 'finished', reply_markup=markup)


# а теперь запускаем проверку в отдельном потоке
p1 = None

bot.polling()
