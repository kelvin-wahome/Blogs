from flask_wtf import FlaskForm
from app.models import Users,Posts,Comments
from wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,RadioField,TextAreaField,IntegerField,SelectField


class Post(FlaskForm):
   '''
   Blog post form.
   '''
   title = StringField('Post', validators=[DataRequired(),Length(min=2,max=140)], render_kw={"placeholder": "Title"})
   content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Article Content"})
   submit = SubmitField('Publish')

class Comment(FlaskForm):
   '''
   Comment form.
   '''
   name = StringField('Name', validators=[DataRequired(),Length(min=2,max=200)], render_kw={"placeholder": "Enter your name"})
   comment = TextAreaField('Comment', validators=[DataRequired(),Length(min=2,max=200)], render_kw={"placeholder": "Have thoughts on the article?"})
   commented_on = IntegerField('Post Id')
   submit = SubmitField('Send')
