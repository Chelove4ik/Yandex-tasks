from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from news_table import DB, UsersModel

app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = DB()


def abort_if_users_not_found(news_id):
    if not UsersModel(db.get_connection()).get(news_id):
        abort(404, message="User {} not found".format(news_id))


parser_put = reqparse.RequestParser()
parser_put.add_argument('user_name')
parser_put.add_argument('password')


class Users(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        user = UsersModel(db.get_connection()).get(user_id)
        return jsonify({'users': user})

    def put(self, user_id):
        args = parser_put.parse_args()
        abort_if_users_not_found(user_id)
        if not args['user_name'] and not args['password']:
            abort(400, message='No data for put')
        UsersModel(db.get_connection()).put(user_id, args['user_name'], args['password'])
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        UsersModel(db.get_connection()).delete(user_id)
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('user_name', required=True)
parser.add_argument('password', required=True)


class UsersList(Resource):
    def get(self):
        user = UsersModel(db.get_connection()).get_all(only_names=True)
        return jsonify({'users': user})

    def post(self):
        args = parser.parse_args()
        users = UsersModel(db.get_connection())
        users.insert(args['user_name'], args['password'])
        return jsonify({'success': 'OK'})


api.add_resource(UsersList, '/', '/users')  # для списка объектов
api.add_resource(Users, '/users/<user_id>')  # для одного объекта

if __name__ == '__main__':
    app.run(port=8080, debug=True)
