from random import choice
from threading import Timer

import telebot
from telebot import types

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')
p1 = None
chat_id = None
slowa = ['Дом', 'Книга', 'Машина', 'Шляпа', 'Бот', 'Дождь', 'Солнце']
words = slowa[:]
teams = [[1, 0], [2, 0]]
team_now = 0
t = 10


def new_game(n_teams=2):
    global teams, words, slowa, team_now
    teams = []
    team_now = 0
    words = slowa[:]
    for i in range(1, n_teams + 1):
        teams.append([i, 0])


def choose_word(msg):
    global words
    if len(words) != 0:
        return words.pop(words.index(choice(words)))
    else:
        return game_over(msg)


def game_over(msg):
    p1.cancel()
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/start')
    teams.sort(key=lambda x: x[1], reverse=True)
    if len(list(filter(lambda x: x[1] == teams[0][1], teams))) > 1:
        bot.send_message(msg.from_user.id, 'Нет победителей', reply_markup=markup)
    else:
        bot.send_message(msg.from_user.id, f'Победитель: {teams[0][0]} команда с {teams[0][1]} очками', reply_markup=markup)


@bot.message_handler(commands=['guessed'])
def guessed(message):
    teams[team_now % 2][1] += 1
    w = choose_word(message)
    if w:
        bot.send_message(message.from_user.id, w)


@bot.message_handler(commands=['next_turn'])
def next(message):
    global team_now
    team_now += 1
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/guessed', '/stop')
    timer(t)
    bot.send_message(message.from_user.id, f'team {teams[team_now % 2][0]} start!', reply_markup=markup)
    w = choose_word(message)
    if w:
        bot.send_message(message.from_user.id, w)


@bot.message_handler(commands=['come_back'])
def back(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/begin')
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=markup)


@bot.message_handler(commands=['stop'])
def stop(message):
    global p1
    p1.cancel()
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/start')
    bot.send_message(message.from_user.id, 'Остановлено', reply_markup=markup)


@bot.message_handler(commands=['begin'])
def begin(message):
    new_game(n_teams=2)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/guessed', '/stop')
    timer(t)
    bot.send_message(message.from_user.id, f'Команда {teams[team_now % 2][0]} начинает', reply_markup=markup)
    w = choose_word(message)
    if w:
        bot.send_message(message.from_user.id, w)


@bot.message_handler(commands=['start'])
def handle_start(message):
    global chat_id
    chat_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/begin')
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=markup)


def timer(x):
    global chat_id, p1
    try:
        p1 = Timer(float(x), callback)
        p1.start()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
        markup.add('/stop')
        bot.send_message(chat_id, 'Начинаю', reply_markup=markup)
    except ValueError:
        return


def callback():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    markup.add('/next_turn')
    bot.send_message(chat_id, f'Команда {teams[team_now % 2][0]} - {teams[team_now % 2][1]} очков', reply_markup=markup)


bot.polling()
