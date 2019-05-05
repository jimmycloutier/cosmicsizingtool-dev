from models import db, basemodel
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class Projects(basemodel.Base):
    __tablename__ = 'projects'
    projectName = db.Column(db.String(255))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

    organization = db.relationship('Organizations', foreign_keys=[organization_id])
    functionalprocesses = db.relationship('FunctionalProcesses', cascade='delete')

    def __repr__(self):
        return self.projectName

    @hybrid_property
    def CFP(self):
        i = 0
        for functionalprocess in self.functionalprocesses:
            i = i + functionalprocess.CFP
        return i

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.projectName,
            'CFP' : self.CFP,
            'org_ID' : self.organization_id,
            'Org' : self.organization.organizationName
        }
