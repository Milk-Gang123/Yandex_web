import datetime

import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
#from data.departament import Departament
from data.jobs import Jobs
from data.users import User
from data.departament import Departament


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
members = []
for dep in db_sess.query(Departament).filter(Departament.id == 1):
    members = dep.members
    members = [i for i in members.split(', ')]
for member in members:
    total_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
    for job in db_sess.query(Jobs).filter(Jobs.collaborators.like(f'%{member}%')):
        date1 = job.start_date
        date2 = job.end_date
        time_delta = date2 - date1
        total_time += time_delta
    if total_time > datetime.timedelta(hours=15):
        user = db_sess.query(User).filter(User.id == int(member)).first()
        print(user.name, user.surname)