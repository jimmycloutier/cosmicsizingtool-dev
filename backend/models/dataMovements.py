from models import db, basemodel
from models.functionalProcesses import FunctionalProcesses, PatternFunctionalProcesses

class DataMovements(basemodel.Base):
    __tablename__ = 'datamovements'
    dmName = db.Column(db.String(255))
    movement = db.Column(db.String(4))

    fp_id = db.Column(db.Integer, db.ForeignKey('functionalprocesses.id'))

    funcprocess = db.relationship('FunctionalProcesses', foreign_keys=[fp_id])

    def __repr__(self):
        return self.dmName

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.dmName,
            'Move' : self.movement,
            'fp_ID' : self.fp_id,
            'FP' : self.funcprocess.fpName
        }

class PatternDataMovements(basemodel.Base):
    __tablename__ = 'patterndatamovements'
    dmName = db.Column(db.String(255))
    movement = db.Column(db.String(4))

    fp_id = db.Column(db.Integer, db.ForeignKey('patternfunctionalprocesses.id'))

    patternfuncprocess = db.relationship('PatternFunctionalProcesses', foreign_keys=[fp_id])

    def __repr__(self):
        return self.dmName

    def to_json(self):
        return {
            'ID' : self.id,
            'Name' : self.dmName,
            'Move' : self.movement,
            'fp_ID' : self.fp_id,
            'FP' : self.patternfuncprocess.fpName
        }