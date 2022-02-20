from urllib import request

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "123"


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня", validators=[DataRequired()])
    submit = SubmitField("Войти")


@app.route('/')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/success")
    param = {"form": form,
             "title": "Авторизация"}
    return render_template('login.html', **param)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")