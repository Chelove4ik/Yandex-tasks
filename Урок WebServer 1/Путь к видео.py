from flask import Flask, url_for

app = Flask(__name__)

video_lst = [
    '<iframe width="962" height="541" src="https://www.youtube.com/embed/eNtK6jx9y4A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    '<iframe width="721" height="541" src="https://www.youtube.com/embed/4PcH6gy8_Ms" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    '<iframe width="962" height="541" src="https://www.youtube.com/embed/cwJKjuyLv80" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    '<iframe width="616" height="493" src="https://www.youtube.com/embed/spDy95Sww6k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    '<iframe width="962" height="541" src="https://www.youtube.com/embed/VMS30oV8ApE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
]


@app.route('/index')
def index():
    return '''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width,
                            initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Привет, Яндекс!</title>
                          </head>
                          <body>
                            <div class="alert alert-primary" role="alert">
                              <h1><u>Привет, Яндекс! Я - Денис</u></h1>
                            </div>
                          </body>
                        </html>'''


@app.route('/image_sample')
def image():
    return '''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width,
                        initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                        crossorigin="anonymous">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <div class="alert alert-primary" role="alert">
                          <h1>Привет, Яндекс! Я - <ins>Денис</ins></h1>
                        </div>
                        <img src="{}" alt="здесь должна была быть картинка, 
                        но не нашлась">
                      </body>
                    </html>'''.format(url_for('static', filename='img/Риана.jpeg'))


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>

                    <nav class="navbar navbar-default">
                      <div class="container-fluid">
                        <!-- Заголовок -->
                        <div class="navbar-header">

                          <!-- Бренд или название сайта (отображается в левой части меню) -->
                          <a class="navbar-brand" href="/index">My site</a>
                        </div>
                        <!-- Основная часть меню (может содержать ссылки, формы и другие элементы) -->
                        <a href="https://www.google.com/search?q=google">google</a>
                        <a href="https://www.google.com/search?q=Коты&tbm=isch">Коты</a>
                        <a href="https://www.google.com/search?q=Собаки&tbm=isch">Собаки</a>
                        <a href="https://www.google.com/search?q=Рекурсия">Рекурсия</a>
                      </div>
                    </nav>


                    <div id="carousel" class="carousel slide" data-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img class="img-fluid" src="{}" alt="изображение не открылось">
                        </div>
                        <div class="carousel-item">
                          <img class="img-fluid" src="{}" alt="изображение не открылось">
                        </div>
                        <div class="carousel-item">
                          <img class="img-fluid"
                           src="https://www.goodfreephotos.com/albums/people/walking-on-the-railroad-tracks.jpg"
                            alt="изображение недоступно">
                        </div>
                      </div>
                    </div>

                    <button type="button" class="btn btn-primary">Не работает</button>
                    <a href="/index" type="button" class="btn btn-primary btn-lg" target="_blank">Работает</a> 

                  </body>
                </html>'''.format(url_for('static', filename='img/Риана.jpeg'),
                                  url_for('static', filename='img/love.jpg'))


@app.route('/text_in_alert/<text>')
def text_in_alert(text):
    return '''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <div class="alert alert-primary" role="alert">
                      <h1>{}</h1>
                    </div>
                  </body>
                </html>'''.format(text)


@app.route('/yandex_music/')
def yandex_music():
    return ''' <h2>Положение</h2>
    <iframe src=https://s174iva.storage.yandex.net/get-mp3/725ea11f0fc04c00ffeff1d4fc481fa9/000584465fcc1702/rmusic/U2FsdGVkX1-OzbzB-y2__g-NAkBWO-WAbXhd-DXu7khQUp5fFlcMtDBu3FrPLPHg7dzv6_vUnacRa9MWy_NPlpybOB7sp8KXe0oq8IpCJ5Y/d45c9afa0e9c098696ab89850b68c9c3235da36fd81db5d7c0812a7ff5ab3466?track-id=48592141&play=true></iframe>'''


@app.route('/list/<num>')
def lst(num):
    return '''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width,
                            initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Привет, Яндекс!</title>
                          </head>
                          <body>
                            <ol>''' + ' '.join(['<li></li>' for _ in range(int(num))]) + '''</ol>
                          </body>
                        </html>'''


@app.route('/table/<int:n>/<int:m>')
def table(n, m):
    listing = []
    for h in range(1, n + 1):
        listing.append(''.join([f'<td>{h},{w}</td>' for w in range(1, m + 1)]))
    pass

    return '''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width,
                            initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Привет, Яндекс!</title>
                          </head>
                          <body>
                            <table class="table table-striped"><tbody><tr>''' + '</tr><tr>'.join(listing) + '''</tr></tbody></table>
                          </body>
                        </html>'''


@app.route('/youtube/<int:num>')
def youtube(num):
    if not 1 <= num <= 5:
        return '<h1>Вы ввели неправильное число</h1>'
    else:
        return str(''.join(video_lst[:num]))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
