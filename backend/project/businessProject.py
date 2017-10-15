from models.projects import  Projects
from models import db
from functionalProcess import BusinessPatternFunctionalProcess, BusinessFunctionalProcess
from dataMovement import BusinessPatternDataMovement, BusinessDataMovement

class BusinessProject(object):
    @staticmethod
    def all_db_projects():
        """Get all projects from database"""
        prjs = Projects.query.all()
        return prjs

    @staticmethod
    def projects(organization_id):
        """Get all projects related to an organization <organization_id>"""
        prjs = Projects.query.filter(Projects.organization_id == organization_id).all()
        return prjs

    @staticmethod
    def create(organization_id, received_project):
        """Create a project related to an organization <organization_id>"""
        if not received_project:
            return

        new_project = Projects(projectName=received_project.Name, organization_id=organization_id)

        db.session.add(new_project)
        db.session.commit()

        return new_project.id

    @staticmethod
    def project(organization_id, project_id):
        """Get a specific projet <project_id>"""
        prj = Projects.query.filter(Projects.id == project_id).first()
        return prj

    @staticmethod
    def update(organization_id, project_id, received_project):
        """Update a specifif project <project_id>"""
        if not received_project:
            return  False

        prj = Projects.query.filter(Projects.id == project_id).first()

        if prj:
            prj.projectName = getattr(received_project, 'Name', prj.projectName)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def delete(organization_id, project_id):
        """Delete a specific project <project_id>"""
        prj = Projects.query.filter(Projects.id == project_id).first()

        if prj:
            db.session.delete(prj)
            db.session.commit()
            return  True
        else:
            return False

    @staticmethod
    def apply_pattern(organization_id, project_id, pattern_id, dmsToRename):
        """
        Apply a pattern to a projet
        JSON request can contain a list of datamovement names that need to be used for the project instead of the one
        specified in the pattern
        """
        fps = BusinessPatternFunctionalProcess.functionalprocesses(pattern_id)

        if not fps:
            return False

        for fp in fps:
            fp_poco = fp.to_poco_obj()
            new_fpId = BusinessFunctionalProcess.create(organization_id, project_id, fp_poco)
            if new_fpId > 0:
                dms = BusinessPatternDataMovement.datamovements(pattern_id, fp.id)
                for dm in dms:
                    dm_poco = dm.to_poco_obj()
                    BusinessDataMovement.create(organization_id, project_id, new_fpId, dm_poco)


        return True