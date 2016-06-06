from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username', [validators.Required(), validators.Length(min=4, max=10)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Password must match'),
        validators.Length(min=4, max=10)
    ])
    confirm = PasswordField('Re Password')

class LoginForm(Form):
    username = StringField('Username', [
        validators.Required(), 
        validators.Length(min=4, max=10)
    ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.Length(min=4, max=10)
    ])