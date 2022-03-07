from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, EmailField
from wtforms.validators import DataRequired


class DepForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    chief_id = IntegerField('Id шефа', validators=[DataRequired()])
    members = StringField('Члены департамента', validators=[DataRequired()])
    email = EmailField('почта департамента', validators=[DataRequired()])
    submit = SubmitField('Войти')