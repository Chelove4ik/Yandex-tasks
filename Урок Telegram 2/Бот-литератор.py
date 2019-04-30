import telebot

bot = telebot.TeleBot('736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ')

sessionStorage = {}
lst = ['qwe', 'rty', 'uio', 'p[]', 'asd', 'fgh', 'jkl', 'zxc', 'vbn', 'm,.']  # чётное кол-во


@bot.message_handler(commands=['start'])
def start(message):
    sessionStorage[message.from_user.id] = 0
    bt(message)


def bt(message):
    if len(lst) == sessionStorage[message.from_user.id]:
        end(message)
        return
    bot.send_message(message.from_user.id, lst[sessionStorage[message.from_user.id]])
    sessionStorage[message.from_user.id] += 1
    bot.register_next_step_handler(message, user)


def user(message):
    if message.text == '/stop':
        end(message)
    elif message.text == lst[sessionStorage[message.from_user.id]]:
        sessionStorage[message.from_user.id] += 1
        bt(message)
    else:
        suphler(message)


def end(message):
    bot.send_message(message.from_user.id,
                     'Чтобы играть снова, пишите /start')
    del sessionStorage[message.from_user.id]


def suphler(message):
    bot.send_message(message.from_user.id, f'Нет, не так. Правильно: {lst[sessionStorage[message.from_user.id]]}')
    bot.register_next_step_handler(message, user)


bot.polling()
