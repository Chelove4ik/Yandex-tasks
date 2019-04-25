import json
import logging

from flask import Flask, request
from geo import get_distance, get_geo_info

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(name)s %(message)s')

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

    logging.info('Request: %r', response)

    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']

    if req['session']['new']:
        res['response']['text'] = 'Привет! Назови свое имя!'
        # созда\м словарь в который в будущем положим имя пользователя
        sessionStorage[user_id] = {
            'first_name': None
        }

        return

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
            sessionStorage[user_id]['first_name'] = first_name.capitalize()
            res['response']['text'] = f'Привет, {sessionStorage[user_id]["first_name"]}! \
            Я могу сказать в какой стране город или сказать расстояние между городами!'
            return

    cities = get_cities(req)

    if len(cities) == 0:

        res['response']['text'] = f'{sessionStorage[user_id]["first_name"]}, Ты не написал название не одного города!'

    elif len(cities) == 1:

        res['response']['text'] = f'{sessionStorage[user_id]["first_name"]}, этот город\
         в стране - ' + get_geo_info(cities[0], 'country')

    elif len(cities) == 2:

        distance = get_distance(get_geo_info(cities[0], 'coordinates'), get_geo_info(cities[1], 'coordinates'))
        res['response']['text'] = f'{sessionStorage[user_id]["first_name"]}, расстояние между этими городами: ' + str(
            round(distance)) + ' км.'

    else:

        res['response']['text'] = f'{sessionStorage[user_id]["first_name"]}, слишком много городов!'


def get_cities(req):
    cities = []

    for entity in req['request']['nlu']['entities']:

        if entity['type'] == 'YANDEX.GEO':

            if 'city' in entity['value'].keys():
                cities.append(entity['value']['city'])

    return cities


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
