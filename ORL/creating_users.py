from flask import Flask
from data import db_session
from data.users import User


def main():
    db_session.global_init("db/blogs.db")
    #for i in range(1, 4):
    #    user = User()
    #    user.name = f"Пользователь {i}"
    #    user.about = f"Биография пользователя"
    #    user.email = f"email{i}@mail.ru"
    #    db_sess = db_session.create_session()
    #    db_sess.add(user)
    #    db_sess.commit()

    # Получение пользователей
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    print(user)

    print(db_sess.query(User).filter(User.id > 1).all())
    # db_sess.query(User).filter(User.id == 3).delete()
    # user = db_sess.query(User).filter(User.id == 2).first
    # db_sess.delete(user)
    # db_sess.commit()

if __name__ == "__main__":
    main()