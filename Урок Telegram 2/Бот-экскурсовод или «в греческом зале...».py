from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

updater = Updater("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")

dp = updater.dispatcher


def main():
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', room1)],

        # Состояние внутри диалога. Вариант с двумя обработчиками,
        # фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.command, room2)],
            3: [MessageHandler(Filters.command, room3)],
            4: [MessageHandler(Filters.command, room4)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(conv_handler)


def room1(bot, update):
    if update.message.text == '/start':
        update.message.reply_text('Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!\n')
    update.message.reply_text(
        'Сейчас Вы находитесь в гардеробе\n'
        'Вы можете пойти /forward, там находится выставка Гоши Будника\n'
        'И можете выйти /back'
    )

    return 2


def room2(bot, update):
    # Это ответ на первый вопрос.
    # Мы можем использовать его во втором вопросе.
    if update.message.text == '/forward':
        update.message.reply_text(
            'Гоша презентует свою новую машину для арктики\n'
            'Вы можете пойти /forward, там находится зал с динозаврами'
        )
        return 3
    elif update.message.text == '/back':
        update.message.reply_text('Досвидания')
        return ConversationHandler.END
    else:
        update.message.reply_text('Такого направления нет')
        return 2


def room3(bot, update):
    if update.message.text == '/forward':
        update.message.reply_text(
            'Вы полюбовались динозаврами\n'
            'Вы можете пойти /forward, там находится столовая\n'
            'И можете пойти /right, там находится гардероб'
        )
        return 4
    else:
        update.message.reply_text('Такого направления нет')
        return 3


def room4(bot, update):
    if update.message.text == '/forward':
        update.message.reply_text(
            'Вы в столовой вкусно поели.\n'
            'Вы можете пойти /right, там находится гардероб'
        )
    elif update.message.text == '/right':
        return room1(bot, update)
    else:
        update.message.reply_text('Такого направления нет')
        return 4


def stop(bot, update):
    update.message.reply_text(
        "Жаль. А было бы интерсно пообщаться. Всего доброго!")
    return ConversationHandler.END  # Константа, означающая конец диалога.


if __name__ == '__main__':
    main()
    updater.start_polling()
    updater.idle()
