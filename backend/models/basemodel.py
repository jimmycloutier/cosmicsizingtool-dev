from models import db

class Base(db.Model):
  __abstract__ = True

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())

  def to_json(self):
      raise NotImplementedError()

  def to_poco_obj(self):
    poco = type('', (), self.to_json())
    return poco