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
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            "news": [item.to_dict() for item in news]
        }
    )


@blueprint.route("/api/jobs/<int:job_id>", methods=['GET'])
def get_jobs_1(job_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(job_id)
    if not news:
        return jsonify({"error": "Not found"})
    return jsonify(
        {
            "news": news.to_dict()
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'work_size', 'job', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    try:
        job = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()
        if job:
            return jsonify({'error': 'Id already exists'})
    except Exception:
        pass
    job = Jobs(
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        job=request.json['job'],
        collaborators=request.json['collaborators'],
        is_finished = request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    if 'team_leader' in request.json:
        job.team_leader=request.json['team_leader']
    if 'work_size' in request.json:
        job.work_size=request.json['work_size']
    if 'job' in request.json:
        job.job=request.json['job']
    if 'collaborators' in request.json:
        job.collaborators=request.json['collaborators']
    if 'is_finished' in request.json:
        job.is_finished = request.json['is_finished']
    if 'start_date' in request.json:
        job.is_finished = request.json['start_date']
    if 'end_date' in request.json:
        job.is_finished = request.json['end_date']
    db_sess.commit()
    return jsonify({'success': 'OK'})