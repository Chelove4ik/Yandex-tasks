import json
from datetime import datetime

from flask import render_template, Flask
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    firstname = StringField('Имя', validators=[InputRequired()])
    secondname = StringField('Фамилия', validators=[InputRequired()])

    question_1 = IntegerField('Сколько Вам лет?', validators=[InputRequired()])
    question_2 = StringField('В каком городе Вы живёте?', validators=[InputRequired()])
    question_3 = StringField('Ссылка на GitHub', validators=[URL()])
    question_4 = StringField('День Вашего рождения DD.MM.YYYY', validators=[InputRequired()])

    submit = SubmitField('Отправить')


@app.route('/little_survey', methods=['GET', 'POST'])
def little_survey():
    form = LoginForm()
    if form.validate_on_submit():
        data = {'data': [{form.firstname.label.text: form.firstname.data,
                          form.secondname.label.text: form.secondname.data,
                          form.question_1.label.text: form.question_1.data,
                          form.question_2.label.text: form.question_2.data,
                          form.question_3.label.text: form.question_3.data,
                          form.question_4.label.text: form.question_4.data}]}
        with open(rf'Users_Answers/{form.firstname.data}_'
                  rf'{form.secondname.data}_{datetime.now().year}_'
                  rf'{datetime.now().month}_{datetime.now().day}_'
                  rf'{datetime.now().hour}_{datetime.now().minute}_'
                  rf'{datetime.now().second}.json', 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
        return redirect('/success')

    return render_template('survey.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'Спасибо за прохождение опроса!'


if __name__ == '__main__':
    app.run()
