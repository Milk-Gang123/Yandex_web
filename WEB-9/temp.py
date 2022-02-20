from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {"username": "Ученик Яндекс.Лицея 42!",
             "title": "Домашняя страница 1501"}
    return render_template('temp.html', **param)


@app.route('/odd-even')
def odd_even():
    param = {"number": 2}
    return render_template('odd_even.html', **param)


@app.route('/news')
def news():
    with open("json/news.json", "rt", encoding="utf-8") as file:
        news_list = json.loads(file.read())
    return render_template('news.html', news=news_list)

@app.route('/queue')
def queue():
    return render_template('queue.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/soft')
def soft():
    return render_template('software.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")