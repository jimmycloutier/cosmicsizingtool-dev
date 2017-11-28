import types
from models import db, basemodel
from models.projects import Projects
from models.patterns import Patterns

class FunctionalProcesses(basemodel.Base):
    __tablename__ = 'functionalprocesses'
    fpName = db.Column(db.String(255))

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    project = db.relationship('Projects', foreign_keys=[project_id])
    datamoves = db.relationship('DataMovements', cascade='delete')

    def __repr__(self):
        return self.fpName

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.fpName,
            'prj_ID' : self.project_id,
            'Prj' : self.project.projectName
        }


class PatternFunctionalProcesses(basemodel.Base):
    __tablename__ = 'patternfunctionalprocesses'
    fpName = db.Column(db.String(255))

    pattern_id = db.Column(db.Integer, db.ForeignKey('patterns.id'))

    pattern = db.relationship('Patterns', foreign_keys=[pattern_id])

    def __repr__(self):
        return self.fpName

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.fpName,
            'ptn_ID' : self.pattern_id,
            'Ptn' : self.pattern.patternName
        }