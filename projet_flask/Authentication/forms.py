from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
from  wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Authentication.models import User
from flask import flash


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min = 2 , max = 20
        )])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min= 4,  message="Ce motde passe n'est pas valide")])
    confirm_password = PasswordField('Confirm the password', validators=[DataRequired(), EqualTo('password', message = "Echec de confirmation")])
    submit = SubmitField('Sign up ')

    def validate_username(self, username):
        info = User.query.filter_by(username = username.data).first()
        if  info:
            raise ValidationError('Ce nom d\'utilisateur est deja pris! ')



    def validate_email(self, email):
        info = User.query.filter_by(email = email.data).first()
        if  info:
            raise ValidationError('Cet email est deja pris! ')


class  LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login ')