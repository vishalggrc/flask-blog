from flask_wtf import Form
from wtforms import validators, StringField
from author.form import RegisterForm

class SetupForm(RegisterForm):
    name = StringField('Blog Name', [
        validators.Required(),
        validators.Length(max=80)
    ])