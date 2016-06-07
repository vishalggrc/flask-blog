from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField
from author.form import RegisterForm
from blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileField, FileAllowed

class SetupForm(RegisterForm):
    name = StringField('Blog Name', [
        validators.Required(),
        validators.Length(max=80)
    ])

def categories():
    return Category.query
    
class PostForm(Form):
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only!')    
    ])
    title = StringField('Title', [
        validators.Required(),
        validators.Length(max=80)
    ])
    body = TextAreaField('Content', validators=[validators.Required()])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('Title')