from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from Таблица_новостей import UsersModel, DB, NewsModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок новости', validators=[DataRequired()])
    content = TextAreaField('Текст новости', validators=[DataRequired()])
    submit = SubmitField('Добавить')


@app.route('/dnevnik', methods=['GET', 'POST'])
def dnevnik():
    form = AddNewsForm()
    if form.validate_on_submit():
        print(*form)
    return render_template('add_news.html', title='Остаток от деления', form=form)


@app.route('/')
def ind():
    db = DB()
    users = NewsModel(db.get_connection())
    return render_template('main.html', news=users.get_all())


if __name__ == '__main__':
    app.run(debug=True)
