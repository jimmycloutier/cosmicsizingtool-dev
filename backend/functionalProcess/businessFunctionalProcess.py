from models.functionalProcesses import  FunctionalProcesses
from models import db

class BusinessFunctionalProcess(object):
    @staticmethod
    def create(organization_id, project_id, fp):
        new_fp = FunctionalProcesses(fpName=fp.Name, project_id=project_id)

        db.session.add(new_fp)
        db.session.commit()

        return new_fp.id

    @staticmethod
    def all_db_functionalprocesses():
        """Get all functional processes from database"""
        fps = FunctionalProcesses.query.all()
        return fps

    @staticmethod
    def functionalprocesses(organization_id, project_id):
        """Get all functional processes related to a specific project <project_id<"""
        fps = FunctionalProcesses.query.filter(FunctionalProcesses.project_id == project_id).all()
        return fps

    @staticmethod
    def functionalprocess(organization_id, project_id, fp_id):
        """Get a specific functional process <fp_id> """
        fp = FunctionalProcesses.query.filter(FunctionalProcesses.id == fp_id).first()
        return fp

    @staticmethod
    def update(organization_id, project_id, fp_id, received_fp):
        """Update a specific functional process <fp_id>"""
        if not received_fp:
            return False

        fp = FunctionalProcesses.query.filter(FunctionalProcesses.id == fp_id).first()

        if fp:
            fp.fpName = getattr(received_fp, 'Name', fp.fpName)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def delete(organization_id, project_id, fp_id):
        """Delete a specific functional process <fp_id>"""
        fp = FunctionalProcesses.query.filter(FunctionalProcesses.id == fp_id).first()

        if fp:
            db.session.delete(fp)
            db.session.commit()
            return True
        else:
            return False








