from models.functionalProcesses import  FunctionalProcesses
from models import db

'''Shared functions between modules'''
class BusinessFunctionalProcess(object):
    @staticmethod
    def create_functionalprocesses(organization_id, project_id, fp):

        new_fp = FunctionalProcesses(fpName=fp.Name, project_id=project_id)

        db.session.add(new_fp)
        db.session.commit()

        return new_fp.id


