from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Esse campo é requirido.")])
    password = PasswordField('Senha', validators=[DataRequired(message="Esse campo é requirido.")])
    remember_me = BooleanField('Lembre de mim')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Esse campo é requirido.")])
    email = StringField('E-mail', validators=[DataRequired(message="Esse campo é requirido."), Email(message="E-mail inválido.")])
    password = PasswordField('Senha', validators=[DataRequired(message="Esse campo é requirido.")])
    password2 = PasswordField(
        'Senha Novamente', validators=[DataRequired(message="Esse campo é requirido."), EqualTo('password', message='Senhas não coincidem.')])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuário já existente.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-mail já existente.')
