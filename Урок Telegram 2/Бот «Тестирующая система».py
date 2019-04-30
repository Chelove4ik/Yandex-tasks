import json
from random import shuffle

import telebot

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')

sessionStorage = {}
with open('data.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)


@bot.message_handler(commands=['start'])
def start(message):
    lst = data['test']
    shuffle(lst)
    sessionStorage[message.from_user.id] = {
        'lst': lst,
        'true': 0
    }
    bot.send_message(message.from_user.id, 'Ответьте на 10 вопросов')
    question(message)


def question(message):
    if len(sessionStorage[message.from_user.id]['lst']) == 0:
        end(message)
        return
    bot.send_message(message.from_user.id, sessionStorage[message.from_user.id]['lst'][0]['question'])
    bot.register_next_step_handler(message, answer)


def answer(message):
    if message.text == sessionStorage[message.from_user.id]['lst'].pop(0)['response']:
        sessionStorage[message.from_user.id]['true'] += 1
        bot.send_message(message.from_user.id, 'Верно')
    else:
        bot.send_message(message.from_user.id, 'Неверно')
    question(message)


@bot.message_handler(commands=['stop'])
def end(message):
    bot.send_message(message.from_user.id,
                     f'Ваш итог: {sessionStorage[message.from_user.id]["true"]}, чтобы играть снова, пишите /start')
    del sessionStorage[message.from_user.id]


bot.polling()
