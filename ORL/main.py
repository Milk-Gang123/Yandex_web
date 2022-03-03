from flask import Flask, render_template, request, abort
from flask_login import login_user
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from ORL.forms.user import LoginForm, RegisterForm
from ORL.forms.job import AddingForm
from ORL.data import db_session
from ORL.data.users import User
from ORL.data.db_session import SqlAlchemyBase, global_init, create_session
from ORL.data.jobs import Jobs
from data import jobs_api

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
        params[f'jobs'].append([job.id, job.job, team_lead, f'{job.work_size} hours', job.collaborators, job.is_finished, user.id])
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
    global_init('db/blogs.db')
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('1')
        global_init('db/blogs.db')
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return  render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template("login.html", title="Авторизация", form=form)


@app.route('/addjob',  methods=['GET', 'POST'])
@login_required
def add_job():
    form = AddingForm()
    if form.validate_on_submit():
        global_init('db/blogs.db')
        try:
            db_sess = db_session.create_session()
            job = Jobs(team_leader=form.team_leader.data,
                       job=form.job.data,
                       work_size=form.work_size.data,
                       collaborators=form.collaborators.data,
                       is_finished=form.is_finished.data)
            db_sess.add(job)
            db_sess.commit()
            return redirect("/")
        except Exception:
            return  render_template('job_adding.html', message="Введены неверные данные", form=form)
    return render_template("job_adding.html", title="Авторизация", form=form)


@app.route('/edit-job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = AddingForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                          ).first()
        if job:
            form.team_leader.data = job.team_leader
            form.job.data = job.job
            form.collaborators.data = job.collaborators
            form.work_size.data = job.work_size
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                         ).first()
        if job:
            job.team_leader = form.team_leader.data
            job.job = form.job.data
            job.collaborators = form.collaborators.data
            job.work_size = form.work_size.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('job_adding.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/delete-job/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id, (Jobs.team_leader == current_user.id) | (current_user.id == 1)).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    a = db_session.__factory
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')