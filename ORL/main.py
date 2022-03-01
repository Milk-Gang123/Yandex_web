from flask import Flask, render_template, request
from flask_login import login_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from ORL.forms.user import LoginForm, RegisterForm
from data import db_session
from data.users import User
from data.db_session import SqlAlchemyBase, global_init, create_session
from data.jobs import Jobs

from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def show_answer():
    params = {'jobs': []}
    global_init('db/blogs.db')
    db_sess = create_session()
    for job in db_sess.query(Jobs).all():
        sess = create_session()
        user = sess.query(User).filter(User.id == job.team_leader).first()
        team_lead = f'{user.name}'
        params[f'jobs'].append([job.id, job.job, team_lead, f'{job.work_size} hours', job.collaborators, job.is_finished])
    return render_template('job_log.html', **params)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        print(form.about.data)
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        global_init('db/blogs.db')
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return  render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template("login.html", title="Авторизация", form=form)




if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")