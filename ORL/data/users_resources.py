from flask import jsonify
from flask_restful import abort, Resource
from . import db_session
from .reqparse import parser
from .users import User


def abort_if_news_not_found(news_id):
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()
    user = session.query(User).get(news_id)
    if not user:
        abort(404, message=f"User {news_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'email', 'about',
                  'city_from')
        )})

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_session.global_init("db/blogs.db")
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'email', 'about',
                  'city_from'))
         for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(name=args['name'],
                    about=args['about'],
                    email=args['email'],
                    hashed_password=args['hashed_password'],
                    city_from=args['city_from'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})