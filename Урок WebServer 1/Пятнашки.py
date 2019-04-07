import os

from PIL import Image
from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/image_puzzle/<int:num>')
def table(num):
    num -= 1
    listing = []
    im = Image.open(r'static/img/Риана.jpeg')
    sx, sy = im.size
    srx, sry = int(sx / 4), int(sy / 4)

    for i in range(4):
        for k in range(4):
            im1 = im.crop((k * srx, i * sry, k * srx + srx, i * sry + sry))
            im1.save('static/img/image{}{}.bmp'.format(i + 1, k + 1))

    for h in range(1, 4 + 1):
        listing.append(''.join(
            [f'<td><img src={url_for("static", filename=f"img/image{h}{w}.bmp")}></td>'
             if (h - 1) * 4 + (w - 1) != num else '<td></td>' for w in range(1, 4 + 1)]))

    for i in range(1, 4 + 1):
        for k in range(1, 4 + 1):
            os.remove(f'static/img/image{i}{k}.bmp')

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
