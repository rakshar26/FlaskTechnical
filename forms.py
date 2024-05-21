
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField


class SignUpForm(FlaskForm):
    number1 = IntegerField('digit1')
    number2 = IntegerField('digit2')
    submit = SubmitField('calculate')
