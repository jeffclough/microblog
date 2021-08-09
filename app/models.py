from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from app import db

class User(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(64),index=True,unique=True)
  email=db.Column(db.String(120),index=True,unique=True)
  password_hash=db.Column(db.String(128))
  posts=db.relationship('Post',backref='author',lazy='dynamic')

  def __repr__(self):
    return f"<User {self.username:r}>"

  def set_password(self,pw):
    self.password_hash=generate_password_hash(pw)

  def check_password(self,pw):
    return check_password_hash(self.password_hash,pw)


class Post(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  body=db.Column(db.String(140))
  timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

  def __repr__(self):
    return f"<Post {self.body:r}>"


# We want "from models import *" to import only our db.Model classes.
__all__=[
  s for s,t in [(x,eval(x)) for x in dir()] if hasattr(t,'__tablename__')
]

