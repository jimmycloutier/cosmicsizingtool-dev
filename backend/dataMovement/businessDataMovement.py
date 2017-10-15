from models.dataMovements import  DataMovements
from models import db
from .datamovement_utils import isValidMove

class BusinessDataMovement(object):
    @staticmethod
    def all_db_datamovements():
        """Get all datamovements from database """
        dms = DataMovements.query.all()
        return dms

    @staticmethod
    def datamovements(organization_id, project_id, fp_id):
        """Get all datamovements for a specific functional process <fp_id>"""
        dms = DataMovements.query.filter(DataMovements.fp_id == fp_id).all()
        return dms

    @staticmethod
    def create(organization_id, project_id, fp_id, received_dm):
        """Create new datamovement for a specific functional process <fp_id>"""
        if not received_dm:
            return

        move = received_dm.Move
        move = move.upper()
        if  not isValidMove(move):
            return

        new_dm = DataMovements(dmName=received_dm.Name, move=move, fp_id=fp_id)

        db.session.add(new_dm)
        db.session.commit()

        return new_dm.id

    @staticmethod
    def datamovement(organization_id, project_id, fp_id, dm_id):
        """Get a specific datamovement <dm_id>"""
        dm = DataMovements.query.filter(DataMovements.id == dm_id).first()

    @staticmethod
    def update(organization_id, project_id, fp_id, dm_id):
        """Update a specific datamovement <dm_id>"""
        if not received_dm:
            return False

        dm = DataMovements.query.filter(DataMovements.id == dm_id).first()

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
    def delete(organization_id, project_id, fp_id, dm_id):
        """Delete a specific data movement <dm_id>"""
        dm = DataMovements.query.filter(DataMovements.id == dm_id).first()

        if dm:
            db.session.delete(dm)
            db.session.commit()
            return True
        else:
            return False
