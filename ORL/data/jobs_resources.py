from flask import jsonify
from flask_restful import abort, Resource
from . import db_session
from .reqparse_jobs import parser
from .jobs import Jobs


def abort_if_jobs_not_found(jobs_id):
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()
    job = session.query(Jobs).get(jobs_id)
    if not job:
        abort(404, message=f"Job {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished')
        )})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        db_session.global_init("db/blogs.db")
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))
         for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        is_fin = ''
        if args['is_finished'] == 'True':
            is_fin = True
        else:
            is_fin = False
        jobs = Jobs(team_leader=args['team_leader'],
                    job=args['job'],
                    work_size=args['work_size'],
                    collaborators=args['collaborators'],
                    is_finished=is_fin)
        print(jobs)
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})