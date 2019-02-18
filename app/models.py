from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Posts(db.Model):

   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String, nullable=False)
   content = db.Column(db.String, nullable=False)
   image = db.Column(db.String, default='post.jpg')
   time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   writer = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   comments = db.relationship('Comments', backref='parent_post', lazy=True)
   link = db.Column(db.String, nullable=False, unique=True)
   def save_post(self):
      '''
      Adds and commits post instance to database
      db.session.add(post)
      db.session.commit()
      '''
      db.session.add(self)
      db.session.commit()

   def delete_post(self):
      '''
      Deletes and commits post instance from database
      db.session.add(post)
      db.session.commit()
      '''
      db.session.delete(self)
      db.session.commit()

   def __repr__(self):
      return f"Posts('{self.title}', '{self.content}', '{self.time}')"


    @classmethod
      def get_post(cls,art_link):
      post = Posts.query.filter_by(link=art_link).first()
      return po
