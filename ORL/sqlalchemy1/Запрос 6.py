import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

from data.users import User
from data.jobs import Jobs

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл БД")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


global_init(input())
db_sess = create_session()
jobs = []
k = 0
for job in db_sess.query(Jobs):
    jobs.append(job)
    if len(job.collaborators.split(', ')) > k:
        k = len(job.collaborators.split(', '))
names = []
for i in jobs:
    if len(i.collaborators.split(', ')) == k:
        id_ = i.team_leader
        db_sess = create_session()
        user = db_sess.query(User).filter(User.id == id_).first()
        if (user.name, user.surname) not in names:
            names.append((user.name, user.surname))
for user in names:
    print(*user)