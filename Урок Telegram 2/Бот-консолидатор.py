import telebot

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')

sessionStorage = {}


@bot.message_handler(commands=['start'])
def start(message):
    sessionStorage[message.from_user.id] = [{}, '']
    bot.send_message(message.from_user.id, 'Привет. Я буду просить у тебя рассказать какой-либо '
                                           'факт о себе, например, сообщить свой любимый цвет, '
                                           'любимою музыкальную группу, количество братьев/сестёр, родной город')
    send_info(message)


def send_info(message):
    bot.send_message(message.from_user.id, 'Введите категорию факта или напишите /stop чтобы узнать всё о себе')
    bot.register_next_step_handler(message, kateg)


def kateg(message):
    if message.text == '/stop':
        end(message)
        return
    sessionStorage[message.from_user.id][1] = message.text
    bot.send_message(message.from_user.id, 'А теперь введите описание факта')
    bot.register_next_step_handler(message, fakt)


def fakt(message):
    if message.text == '/stop':
        end(message)
        return
    kat = sessionStorage[message.from_user.id][1]
    sessionStorage[message.from_user.id][0][kat] = message.text
    bot.send_message(message.from_user.id, 'Я записал!')
    send_info(message)


def end(message):
    bot.send_message(message.from_user.id, '\n'.join(
        f'{i}:{sessionStorage[message.from_user.id][0][i]}' for i in sessionStorage[message.from_user.id][0].keys()))
    del sessionStorage[message.from_user.id]


bot.polling()
