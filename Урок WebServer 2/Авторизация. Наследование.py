import json

from flask import render_template, Flask
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    log = False
    if form.validate_on_submit():
        with open("passwords.json", encoding="utf8") as f:
            data = json.loads(f.read())['passwords']
        for i in data:
            if i['login'] == form.username.data:
                log = True
                if i['password'] == form.password.data:
                    return redirect('/success')
        if log:
            return 'Неверный пароль'
        else:
            return 'Неверный логин'
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'Вы вошли'


if __name__ == '__main__':
    app.run()
