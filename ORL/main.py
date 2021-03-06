import requests
from flask import Flask, render_template, request, abort, make_response, jsonify
from flask_login import login_user
from flask_restful import Api
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from forms.user import LoginForm, RegisterForm
from forms.job import AddingForm
from forms.dep import DepForm
from data import db_session
from data.users import User
from data.db_session import SqlAlchemyBase, global_init, create_session
from data.jobs import Jobs
from data import jobs_api
from data import user_api
from data.departament import Departament
from data import users_resources
from data import jobs_resources


from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app, catch_all_404s=True)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def show_jobs():
    params = {'jobs': []}
    global_init('db/blogs.db')
    db_sess = create_session()
    for job in db_sess.query(Jobs).all():
        sess = create_session()
        user = sess.query(User).filter(User.id == job.team_leader).first()
        team_lead = f'{user.name}'
        params[f'jobs'].append([job.id, job.job, team_lead, f'{job.work_size} hours', job.collaborators, job.is_finished, user.id])
    return render_template('job_log.html', **params)


@app.route('/dep_log')
def show_deps():
    params = {'deps': []}
    global_init('db/blogs.db')
    db_sess = create_session()
    for dep in db_sess.query(Departament).all():
        sess = create_session()
        user = sess.query(User).filter(User.id == dep.chief_id).first()
        team_lead = f'{user.name}'
        params[f'deps'].append([dep.id, dep.title, team_lead, dep.members, dep.email, user.id])
    return render_template('dep_log.html', **params)


@app.route('/dep_adding', methods=['GET', 'POST'])
def add_deps():
    form = DepForm()
    if form.validate_on_submit():
        global_init('db/blogs.db')
        try:
            db_sess = db_session.create_session()
            dep = Departament(title=form.title.data,
                              chief_id=form.chief_id.data,
                              members=form.members.data,
                              email=form.email.data)
            db_sess.add(dep)
            db_sess.commit()
            return redirect("/dep_log")
        except Exception as e:
            print(e)
            return render_template('dep_adding.html', message="?????????????? ???????????????? ????????????", form=form)
    return render_template("dep_adding.html",  form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='??????????????????????', form=form,
                                   message="???????????? ???? ??????????????????")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='??????????????????????', form=form,
                                   message="?????????? ???????????????????????? ?????? ????????")
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
    return render_template('register.html', title='??????????????????????', form=form)


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
        global_init('db/blogs.db')
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return  render_template('login.html', message="???????????????????????? ?????????? ?????? ????????????", form=form)
    return render_template("login.html", title="??????????????????????", form=form)


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
            return  render_template('job_adding.html', message="?????????????? ???????????????? ????????????", form=form)
    return render_template("job_adding.html", title="??????????????????????", form=form)


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
                           title='???????????????????????????? ??????????????',
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


@app.route('/users_show/<int:user_id>')
def show_user(user_id):
    try:
        response = requests.get(f'http://127.0.0.1:8080/api/users_show/{user_id}')
        print(response)
        if response == 'Error':
            abort(404)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        params = {'name': user.name, 'address': user.city_from}
        return render_template('user_show.html', **params)
    except Exception as e:
        print(e)
        return 'aaa'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)



if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(jobs_resources.JobsListResource, '/api/v2/jobs')
    api.add_resource(jobs_resources.JobsResource, '/api/v2/jobs/<int:jobs_id>')
    app.register_blueprint(user_api.blueprint)
    app.run(port=8080, host='127.0.0.1')