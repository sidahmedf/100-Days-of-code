from cProfile import label
import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    pwd = PasswordField(label='Password', validators=[Length(8,12)])
    submit = SubmitField(label='Submit')