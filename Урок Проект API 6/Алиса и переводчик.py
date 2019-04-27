import json
import logging

from flask import Flask, request
from requests import get

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(name)s %(message)s')


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
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я могу сделать перевод на английский язык'

    elif 'переведи слово' in req['request']['command']:
        res['response']['text'] = translate(req['request']['command'][15:])
    else:
        res['response']['text'] = 'Я тебя не поняла. Попробуй "Переведи слово <слово>"'


def translate(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    param = {
        'key': 'trnsl.1.1.20190427T100302Z.81d7d299b06261b2.9452dc6a4d8aae7dc4e0980fdf76cd383858c21f',
        'text': text,
        'lang': 'en'
    }

    return get(url, param).json()['text'][0]


if __name__ == '__main__':
    app.run()
