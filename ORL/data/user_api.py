import flask
import requests
from flask import request, jsonify
from . import db_session
from .users import User


blueprint = flask.Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)


@blueprint.route("/api/users")
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            "users": [item.to_dict() for item in users]
        }
    )


@blueprint.route("/api/users/<int:user_id>", methods=['GET'])
def get_users_1(user_id):
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(user_id)
    if not news:
        return jsonify({"error": "Not found"})
    return jsonify(
        {
            "user": news.to_dict()
        }
    )

@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'about', 'email', 'hashed_password']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    try:
        user = db_sess.query(User).filter(User.id == request.json['id']).first()
        if user:
            return jsonify({'error': 'Id already exists'})
    except Exception:
        pass
    print(request.json['hashed_password'])
    user = User()
    user.name=request.json['name']
    user.about=request.json['about']
    user.email=request.json['email']
    user.hashed_password=request.json['hashed_password']
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_jobs(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_jobs(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    if 'name' in request.json:
        user.name=request.json['name']
    if 'about' in request.json:
        user.about=request.json['about']
    if 'email' in request.json:
        user.email=request.json['email']
    if 'hashed_password' in request.json:
        user.hashed_password=request.json['hashed_password']
    if 'created_date' in request.json:
        user.created_date = request.json['created_date']
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users_show/<int:user_id>', methods=['GET'])
def show_us(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return 'Error'
    address = user.city_from
    search_api_server = "http://static-maps.yandex.ru/1.x/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    adr_req = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"
    adr_resp = requests.get(adr_req).json()
    address_ll = ','.join(
        adr_resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
    search_params = {
        "apikey": api_key,
        "ll": address_ll,
        "l": 'sat',
        "format": "json",
        "spn": f'0.1,0.1'
    }
    response = requests.get(search_api_server, params=search_params)
    map_file = "static/img/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return 'Success'