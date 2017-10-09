from models import db, basemodel
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_login import UserMixin


class Users(basemodel.Base, UserMixin):
  __tablename__ = 'users'
  email = db.Column(db.String(100), unique=True)
  username = db.Column(db.String(50), unique=True)
  password = db.Column(db.String(300))

  def __repr__(self):
    return self.username

class OAuth(OAuthConsumerMixin, db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship('Users', foreign_keys = [user_id])

