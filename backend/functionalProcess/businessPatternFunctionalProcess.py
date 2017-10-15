from models.functionalProcesses import  PatternFunctionalProcesses
from models import db


class BusinessPatternFunctionalProcess(object):
    @staticmethod
    def functionalprocesses(pattern_id):
        return PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.pattern_id == pattern_id).all()

    @staticmethod
    def all_db_patternfunctionalprocesses():
        """Get all functional processes related to pattern from database"""
        pfps = PatternFunctionalProcesses.query.all()
        return pfps

    @staticmethod
    def create(pattern_id, received_fp):
        """Create a new functional process for a pattern <pattern_id> """
        new_fp = PatternFunctionalProcesses(fpName=received_fp.Name, pattern_id=pattern_id)

        db.session.add(new_fp)
        db.session.commit()

        return new_fp.id

    @staticmethod
    def patternfunctionalprocess(pattern_id, fp_id):
        """Get a specific functional process <fp_id>(related to a Pattern)"""
        fp = PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.id == fp_id).first()
        return fp

    @staticmethod
    def update(pattern_id, fp_id, received_fp):
        """Update a specific functional process <fp_id> (related to a pattern)"""
        if not received_fp:
            return  False

        fp = PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.id == fp_id).first()

        if fp:
            fp.fpName = getattr(received_fp, 'Name', fp.fpName)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def delete(project_id, fp_id):
        """Delete a specific functional process <fp_id> (related to a pattern)"""
        fp = PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.id == fp_id).first()

        if fp:
            db.session.delete(fp)
            db.session.commit()
            return True
        else:
            return False



