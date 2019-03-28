from flask import render_template, Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NoneOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    first = IntegerField('Первое', validators=[InputRequired()])
    second = IntegerField('Второе', validators=[InputRequired(), NoneOf([0], message='Делить на 0 нельзя')])
    submit = SubmitField('Отправить')


@app.route('/div_mod', methods=['GET', 'POST'])
def div_mod():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Делится без остатка' if form.first.data % form.second.data == 0 else 'Не делится без остатка'
    return render_template('div_mod.html', title='Остаток от деления', form=form)


if __name__ == '__main__':
    app.run()
