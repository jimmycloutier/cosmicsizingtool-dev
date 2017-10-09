from models import db, basemodel

class Patterns(basemodel.Base):
    __tablename__ = 'patterns'
    patternName = db.Column(db.String(255))

    def __repr__(self):
        return self.patternName

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.patternName
        }
