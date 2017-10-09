from models import db, basemodel

class Organizations(basemodel.Base):
    __tablename__ = 'organizations'
    organizationName = db.Column(db.String(255))
    organizationURL = db.Column(db.String(255))

    def __repr__(self):
        return self.organizationName

    def to_json(self):
        return {
                'ID' : self.id,
                'Name' : self.organizationName,
                'URL' : self.organizationURL
        }
