from functools import wraps

from admins import AdminsModel
from flask import render_template, Flask, session
from flask_wtf import FlaskForm
from news_table import DB, NewsModel, UsersModel
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms import TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db = DB()


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок новости', validators=[DataRequired()])
    content = TextAreaField('Текст новости', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class ButtonForm(FlaskForm):
    sortd = RadioField('Label', choices=[(False, 'По времени добавления'), (True, 'По алфавиту')])


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login')
        return f(*args, **kwargs)

    return decorated_function


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user_name = form.username.data
        password = form.password.data
        user_model = UsersModel(db.get_connection())
        admin_model = AdminsModel(db.get_connection())
        exists = user_model.exists(user_name, password)
        exists_adm = admin_model.exists(user_name, password)
        if exists[0]:
            session['username'] = user_name
            session['user_id'] = exists[1]
            session['is_admin'] = False
        elif exists_adm[0]:
            session['username'] = user_name
            session['user_id'] = exists_adm[1]
            session['is_admin'] = True
        return redirect("/index")

    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    session.pop('username', 0)
    session.pop('user_id', 0)
    return redirect('/login')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    news = NewsModel(db.get_connection()).get_all(session['user_id'])
    form = ButtonForm()
    if form.is_submitted():
        if form.sortd.data == 'True':
            news.sort(key=lambda i: i[1])
        else:
            news.sort()
        return render_template('main.html', username=session['username'],
                               news=news, form=form)

    return render_template('main.html', username=session['username'],
                           news=news, form=form)


@app.route('/add_news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = AddNewsForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        nm = NewsModel(db.get_connection())
        nm.insert(title, content, session['user_id'])
        return redirect("/index")
    return render_template('add_news.html', title='Добавление новости',
                           form=form, username=session['username'])


@app.route('/delete_news/<int:news_id>', methods=['GET'])
@login_required
def delete_news(news_id):
    nm = NewsModel(db.get_connection())
    nm.delete(news_id)
    return redirect("/index")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_model = UsersModel(db.get_connection())
        user_model.insert(user_name, password)
        return redirect("/login")

    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/admin_page')
@login_required
def admin_page():
    if not session['is_admin']:
        return redirect("/")
    users = UsersModel(db.get_connection()).get_all()
    news = NewsModel(db.get_connection())

    return render_template('admin_page.html', title='Информация о пользователях', users=users, news=news)


if __name__ == '__main__':
    app.run(debug=True)
# www.menti.com   68 30 27
