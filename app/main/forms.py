from flask_wtf import FlaskForm
from app.models import User,Blog,Comment
from wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,RadioField,TextAreaField,IntegerField,SelectField


class Blog(FlaskForm):
   '''
   Blog post form.
   '''
   title = StringField('Blog', validators=[DataRequired(),Length(min=2,max=140)], render_kw={"placeholder": "Title"})
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

class Bio(FlaskForm):
   '''
   Update bio.
   '''
   bio = TextAreaField('Bio', validators=[DataRequired()], render_kw={"placeholder": "Write something about yourself"})
   submit = SubmitField('Update Bio')
