import datetime
from data import db_session
from data.users import User


def main():
    db_session.global_init("db/blogs.db")
    job = User()
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == "__main__":
    main()