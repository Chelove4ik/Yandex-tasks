import json
import logging
import random

from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# создаём словарь, в котором ключ — название города, а значение — массив,
# где перечислены id картинок, которые мы записали в прошлом пункте.
cities = {
    'москва': [
        '937455/dbaf9d11c2f195b00728', '1652229/e05eaa323b00acc46dd0'
    ],
    'нью-йорк': [
        '937455/191c7b66a90e936544cc', '965417/e5c5a62e0ae083da4e64'
    ],
    'париж': [
        '965417/b2a60100922dcab7d666', '1652229/373b7c0d4f1ff917c71b'
    ]
}

# создаём словарь, где для каждого пользователя мы будем хранить его имя
sessionStorage = {}


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Response: %r', response)
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']

    # если пользователь новый, то просим его представиться.
    if req['session']['new']:
        res['response']['text'] = 'Привет! Назови свое имя!'
        # созда\м словарь в который в будущем положим имя пользователя
        sessionStorage[user_id] = {
            'first_name': None
        }
        return

    # если пользователь не новый, то попадаем сюда.
    # если поле имени пустое, то это говорит о том,
    # что пользователь ещё не представился.
    if sessionStorage[user_id]['first_name'] is None:
        # в последнем его сообщение ищем имя.
        first_name = get_first_name(req)
        # если не нашли, то сообщаем пользователю что не расслышали.
        if first_name is None:
            res['response']['text'] = \
                'Не расслышала имя. Повтори, пожалуйста!'
        # если нашли, то приветствуем пользователя.
        # И спрашиваем какой город он хочет увидеть.
        else:
            sessionStorage[user_id]['first_name'] = first_name
            res['response'][
                'text'] = 'Приятно познакомиться, ' + first_name.title() \
                          + '. Я - Алиса. Какой город хочешь увидеть?'
            # получаем варианты buttons из ключей нашего словаря cities

    # если мы знакомы с пользователем и он нам что-то написал,
    # то это говорит о том, что он уже говорит о городе, что хочет увидеть.
    else:
        city = get_city(req)
        if req['request']['command'] == 'Помощь':
            res['response']['text'] = 'Эта игра - Угадай город. \
            Правила очень просты: Вы отправляете название города, \
            а я Вам картинку этого города, если знаю его'
        # ищем город в сообщение от пользователя
        # если этот город среди известных нам,
        # то показываем его (выбираем одну из двух картинок случайно)
        elif city in cities:
            res['response']['card'] = {}
            res['response']['card']['type'] = 'BigImage'
            res['response']['card']['title'] = 'Этот город я знаю.'
            res['response']['card']['image_id'] = random.choice(
                cities[city])
            res['response']['text'] = 'Я угадал!'
        # если не нашел, то отвечает пользователю
        # 'Первый раз слышу об этом городе.'
        else:
            res['response']['text'] = \
                'Первый раз слышу об этом городе. Попробуй еще разок!'
    res['response']['buttons'] = [
        {
            'title': city.title(),
            'hide': True
        } for city in cities
    ]
    res['response']['buttons'].append({
        'title': 'Помощь',
        'hide': True
    })


def get_city(req):
    # перебираем именованные сущности
    for entity in req['request']['nlu']['entities']:
        # если тип YANDEX.GEO то пытаемся получить город(city),
        # если нет то возвращаем None
        if entity['type'] == 'YANDEX.GEO':
            # возвращаем None, если не нашли сущности с типом YANDEX.GEO
            return entity['value'].get('city', None)


def get_first_name(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name',
            # то возвращаем ее значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)


if __name__ == '__main__':
    app.run()
