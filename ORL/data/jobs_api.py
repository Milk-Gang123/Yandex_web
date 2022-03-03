import flask
from flask import request, jsonify
from ORL.data import db_session
from ORL.data.jobs import Jobs


blueprint = flask.Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)


@blueprint.route("/api/jobs")
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            "news": [item.to_dict() for item in news]
        }
    )


@blueprint.route("/api/news/<int:news_id>", methods=['GET'])
def get_news_1(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(news_id)
    if not news:
        return jsonify({"error": "Not found"})
    return jsonify(
        {
            "news": news.to_dict(only=("title", "content", "user_id", "is_private"))
        }
    )

@blueprint.route('/api/news', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    news = Jobs(
        title=request.json['title'],
        content=request.json['content'],
        user_id=request.json['user_id'],
        is_private=request.json['is_private']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})