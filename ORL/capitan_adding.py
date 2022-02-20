from data import db_session
from data.users import User


def main():
    db_session.global_init("db/blogs.db")
    capitan = User()
    capitan.surname = 'Scott'
    capitan.name = "Ridley"
    capitan.age = 21
    capitan.position = "captain"
    capitan.speciality = "research engineer"
    capitan.address = "module_1"
    capitan.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(capitan)
    db_sess.commit()
    names = {1: 'John', 2: 'Mark', 3: 'Alex'}
    surnames = {1: 'Rumanov', 2: 'Korolev', 3: 'Ushveridze'}
    ages = {1: 25, 2: 20, 3: 15}
    profs = {1: 'Driver', 2: 'Scientist', 3: 'Defender'}
    for i in range(1, 4):
        user = User()
        user.surname = surnames[i]
        user.name = names[i]
        user.age = ages[i]
        user.position = "astronaut"
        user.speciality = profs[i]
        user.address = f"module_2.{i}"
        user.email = f"user{i}@mars.org"
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()


if __name__ == "__main__":
    main()