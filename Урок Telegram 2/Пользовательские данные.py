from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

updater = Updater("736529129:AAFfzgvqN5RwiLcRskGxb0agCul1I_7FehQ")

dp = updater.dispatcher


def main():
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога. Вариант с двумя обработчиками,
        # фильтрующими текстовые сообщения.
        states={
            # Добавили user_data для сохранения ответа.
            1: [MessageHandler(Filters.text, first_response,
                               pass_user_data=True)],
            # ...и для его использования.
            2: [MessageHandler(Filters.text, second_response,
                               pass_user_data=True)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(conv_handler)


def start(bot, update):
    update.message.reply_text(
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать опрос, послав команду /stop.\n"
        "В каком городе вы живёте?")

    # Число-ключ в словаре states —
    # втором параметре ConversationHandler'а.
    return 1
    # Оно указывает, что дальше на сообщения
    # от этого пользователя должен отвечать обработчик states[1].
    # До этого момента обработчиков текстовых сообщений
    # для этого пользователя не существовало,
    # поэтому текстовые сообщения игнорировались.


# Добавили словарь user_data в параметры.
def first_response(bot, update, user_data):
    # Сохраняем ответ в словаре.
    user_data['locality'] = update.message.text
    update.message.reply_text(
        "Какая погода в городе {0}?".format(
            user_data['locality']))
    return 2


# Добавили словарь user_data в параметры.
def second_response(bot, update, user_data):
    weather = update.message.text
    # Используем user_data в ответе.
    update.message.reply_text(
        "Спасибо за участие в опросе! Привет, {0}!".format(
            user_data['locality']))
    return ConversationHandler.END


def stop(bot, update):
    update.message.reply_text(
        "Жаль. А было бы интерсно пообщаться. Всего доброго!")
    return ConversationHandler.END  # Константа, означающая конец диалога.


if __name__ == '__main__':
    main()
    updater.start_polling()
    updater.idle()
