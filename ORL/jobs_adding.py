import datetime
from data import db_session
from data.jobs import Jobs


def main():
    db_session.global_init("db/blogs.db")
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.end_date = job.start_date + datetime.timedelta(hours=job.work_size)
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == "__main__":
    main()