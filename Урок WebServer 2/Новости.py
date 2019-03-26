import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/news')
def news():
    with open("news.json", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)


if __name__ == '__main__':
    app.run()
