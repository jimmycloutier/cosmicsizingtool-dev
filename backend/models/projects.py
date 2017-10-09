from models import db, basemodel
from models.organizations import Organizations

class Projects(basemodel.Base):
    __tablename__ = 'projects'
    projectName = db.Column(db.String(255))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

    organization = db.relationship('Organizations', foreign_keys=[organization_id])

    def __repr__(self):
        return self.projectName

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.projectName,
            'org_ID' : self.organization_id,
            'Org' : self.organization.organizationName
        }
