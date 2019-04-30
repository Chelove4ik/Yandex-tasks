import json

import telebot

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')


def check_number(num: str):
    number = ''
    for i in num:
        if i.isdigit():
            number += i
    if number[0] == '8':
        number = '+7' + number[1::]
    else:
        number = '+' + number
    return number


def write_number(num: str):
    num = check_number(num)
    number = num[0:2] + '-' + num[2:5] + '-' + num[5:8] + '-' + num[8::]
    return number


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    with open('data.json', mode='r', encoding='utf8') as f:
        data = json.load(f)
    if ':' in message.text:
        register_phone(message)
    for i in data:
        if i['name'] == message.text:
            bot.send_message(message.from_user.id, i['phone'])
        elif i['phone'] == write_number(message.text):
            bot.send_message(message.from_user.id, i['name'])


def register_phone(message):
    t = message.text.split(':')
    with open('data.json', mode='r', encoding='utf8') as f:
        data = json.load(f)
    data.append({'name': t[0].strip(), 'phone': t[1].strip()})
    with open('data.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile)
    bot.send_message(message.from_user.id, 'Добавлено')


bot.polling()
