from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddingForm(FlaskForm):
    team_leader = IntegerField('id тимлидера', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Длительость работы', validators=[DataRequired()])
    collaborators = StringField('Список помощников', validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена')
    submit = SubmitField('Войти')