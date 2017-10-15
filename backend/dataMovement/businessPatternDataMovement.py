from models.dataMovements import  PatternDataMovements
from models import db
from .datamovement_utils import isValidMove

class BusinessPatternDataMovement(object):

    @staticmethod
    def datamovements(pattern_id, fp_ip):
        return PatternDataMovements.query.filter(PatternDataMovements.fp_id == fp_ip).all()

    @staticmethod
    def create(pattern_id, fp_id, received_dm):
        """Create new datamovement for a specific functional process (realted to a pattern) <fp_id>"""
        if not received_dm:
            return

        move = received_dm.Move
        move = move.upper()
        if  not isValidMove(move):
            return

        new_dm = PatternDataMovements(dmName=received_dm.Name, move=move, fp_id=fp_id)

        db.session.add(new_dm)
        db.session.commit()

        return new_dm.id

    @staticmethod
    def datamovement(pattern_id, fp_id, dm_id):
        """Get a specific datamovement (related to a pattern) <dm_id>"""
        dm = PatternDataMovements.query.filter(PatternDataMovements.id == dm_id).first()
        return dm


    @staticmethod
    def update(pattern_id, fp_id, dm_id, received_dm):
        """Update a specific datamovement (related to a pattern) <dm_id>"""
        if not received_dm:
            return False

        dm = PatternDataMovements.query.filter(PatternDataMovements.id == dm_id).first()

        if dm:
            dm.dmName = getattr(received_dm, 'Name', dm.dmName)

            move = getattr(received_dm, 'Move', dm.movement)
            if move:
                move = move.upper()
                if isValidMove(move):
                    dm.movement = move

            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def delete(project_id, fp_id, dm_id):
        """Delete a specific data movement (related to a pattern) <dm_id>"""
        dm = PatternDataMovements.query.filter(PatternDataMovements.id == dm_id).first()

        if dm:
            db.session.delete(dm)
            db.session.commit()
            return True
        else:
            return False