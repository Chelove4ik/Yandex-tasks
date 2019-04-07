from flask import Flask, jsonify
from flask import make_response
from flask import request
from news_table import DB, NewsModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = DB()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/news', methods=['PUT'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or 'user_id' not in request.json:
        return jsonify({'error': 'Bad request'})
    if 'title' not in request.json:
        request.json['title'] = None
    if 'content' not in request.json:
        request.json['content'] = None
    news = NewsModel(db.get_connection())
    news.put(request.json['id'], request.json['title'],
             request.json['content'], request.json['user_id'])
    return jsonify({'success': 'OK'})


@app.route('/news', methods=['GET'])
def get_news():
    news = NewsModel(db.get_connection()).get_all()
    return jsonify({'news': news})


if __name__ == '__main__':
    app.run(port=8080, debug=True)
