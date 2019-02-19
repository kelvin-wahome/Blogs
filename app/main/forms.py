from flask_wtf import FlaskForm
from app.models import User, Blog, Comment
from wtforms.validators import Required,Email,EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, RadioField, TextAreaField, IntegerField, SelectField


class Blog(FlaskForm):
    '''
    Blog post form.
    '''
    title = StringField('Title ')
    description = TextAreaField('Blog Content')
    submit = SubmitField('Publish')


class Comment(FlaskForm):
    '''
    Comment form.
    '''
    name = StringField('Name', validators=[Required()])
    content = TextAreaField('Add comment', validators=[Required()])
    submit = SubmitField()


class UpdateForm(FlaskForm):
    title = StringField('Title for you Blog', validators=[Required()])
    description = TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Edit')
