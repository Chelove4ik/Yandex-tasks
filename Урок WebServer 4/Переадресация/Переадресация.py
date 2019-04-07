from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from news_table import DB, NewsModel

app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = DB()


def abort_if_news_not_found(news_id):
    if not NewsModel(db.get_connection()).get(news_id):
        abort(404, message="News {} not found".format(news_id))


class News(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        news = NewsModel(db.get_connection()).get(news_id)
        return jsonify({'news': news})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        NewsModel(db.get_connection()).delete(news_id)
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('user_id', required=True, type=int)


class NewsList(Resource):
    def get(self):
        news = NewsModel(db.get_connection()).get_all(only_titles=True)
        return jsonify({'news': news})

    def post(self):
        args = parser.parse_args()
        news = NewsModel(db.get_connection())
        news.insert(args['title'], args['content'], args['user_id'])
        return jsonify({'success': 'OK'})


api.add_resource(NewsList, '/', '/news')  # для списка объектов
api.add_resource(News, '/news/<news_id>')  # для одного объекта

if __name__ == '__main__':
    app.run(port=8080, debug=True)
