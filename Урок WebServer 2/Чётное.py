from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/odd_even', methods=['POST', 'GET'])
def sample_file_upload():
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
                            <title>Имя</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="about">Введите число</label>
                                    <textarea class="form-control" id="about" rows="1" name="chislo"></textarea>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        num = request.form.get('chislo')
        try:
            if int(num) == float(num):
                return render_template('odd_even.html', number=int(num))
            else:
                return f'{num} не является корректным целым числом'
        except Exception:
            return f'{num} не является корректным целым числом'


if __name__ == '__main__':
    app.run()
