from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar_me = BooleanField('Lembrar-me')
    acessar = SubmitField('Acessar')