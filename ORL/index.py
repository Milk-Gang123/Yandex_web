from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

from data import db_session
from data.users import User
from data.db_session import SqlAlchemyBase, global_init, create_session
from data.jobs import Jobs

#from flask_login import LoginManager


app = Flask(__name__)
#login_manager = LoginManager()
#login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def show_answer():
    params = {'jobs': []}
    global_init('db/blogs.db')
    db_sess = create_session()
    for job in db_sess.query(Jobs).all():
        sess = create_session()
        user = sess.query(User).filter(User.id == job.team_leader).first()
        team_lead = f'{user.name} {user.surname}'
        params[f'jobs'].append([job.id, job.job, team_lead, f'{job.work_size} hours', job.collaborators, job.is_finished])
    return render_template('job_log.html', **params)


@app.route('/register', methods=['POST', 'GET'])
def show_form():
    global FORM_DATA
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        user = User()
        print(1)
        if request.form['password1'] == request.form['password2']:
            print(2)
            user.email = request.form['email']
            user.surname = request.form['surname']
            user.name = request.form['name']
            user.age = request.form['age']
            user.position = request.form['position']
            user.speciality = request.form['speciality']
            user.address = request.form['address']
            user.hashed_password = str(generate_password_hash(request.form['password1']))
            global_init('db/blogs.db')
            db_sess = create_session()
            db_sess.add(user)
            db_sess.commit()
            return "Данные успешно сохранены"
        else:
            return "Введенные пароли не совпадают, данные не сохранены"




if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")