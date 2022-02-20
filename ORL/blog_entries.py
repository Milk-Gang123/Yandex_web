from flask import Flask
from data import db_session
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KGBSDJK'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    news = News()
    news.title = f"Первая новость"
    news.content = f"Привет блог"
    news.user_id = 1
    news.is_private = False
    db_sess.add(news)
    db_sess.commit()


if __name__ == "__main__":
    main()