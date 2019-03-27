from flask import Flask, request

app = Flask(__name__)


@app.route('/greeting_form', methods=['GET', 'POST'])
def greeting_form():
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
                                    <h1>Форма для приветствия в суперсекретной системе</h1>
                                    <form method="post">
                                        <div class="form-group">
                                            <label for="about">Введите ваше имя</label>
                                            <textarea class="form-control" id="about" rows="1" name="name"></textarea>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                  </body>
                                </html>'''
    elif request.method == 'POST':
        return 'Привет, ' + request.form.get('name')


if __name__ == '__main__':
    app.run()
