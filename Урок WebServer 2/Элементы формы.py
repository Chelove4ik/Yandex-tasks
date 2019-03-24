from flask import Flask, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <form method="post">
                                <div class="form-group">
                                    <label for="about">Немного о себе</label>
                                    <textarea class="form-control" id="about" rows="1" name="about_1"></textarea>
                                </div>

                                <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                
                                <div class="form-group">
                                    <label for="about">Немного о себе</label>
                                    <textarea class="form-control" id="about" rows="3" name="about_3"></textarea>
                                </div>
                                
                                <div class="form-group">
                                    <label for="classSelect">Кто лучше?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>Денис</option>
                                      <option>Дени</option>
                                      <option>Данил</option>
                                      <option>Даниил</option>
                                      <option>Даниииииииил</option>
                                    </select>
                                 </div>
                                 
                                 <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                                 
                                 <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Даю согласие на обработку персональных данных</label>
                                </div>
                                
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('about_1'))
        print(request.form.get('password'))
        print(request.form.get('about_3'))
        print(request.form.get('class'))
        print(request.form.get('sex'))
        print(request.form.get('accept'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run()
