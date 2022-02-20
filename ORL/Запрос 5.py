import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
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
for job in db_sess.query(Jobs).filter(Jobs.is_finished == 0, Jobs.work_size < 20):
    print(f"<Job> {job.job}")