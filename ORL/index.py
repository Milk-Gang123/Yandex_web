from flask import Flask, render_template
from data import db_session
from data.users import User
from data.db_session import SqlAlchemyBase, global_init, create_session
from data.jobs import Jobs


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def show_answer():
    global_init('db/blogs.db')
    db_sess = create_session()
    for job in db_sess.query(Jobs).all():
        print(job)
    return render_template('job_log.html')


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")