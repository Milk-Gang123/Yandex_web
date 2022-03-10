from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, make_response, jsonify
from data import db_session, news_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret'
api = Api(app, catch_all_404s=True)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    app.run(port=8080, host="127.0.0.1")

if __name__ == "__main__":
    main()