from models.patterns import  Patterns
from models import db

class BusinessPattern(object):
    @staticmethod
    def all_db_patterns():
        """Get all patterns from database"""
        ptns = Patterns.query.all()
        return ptns

    @staticmethod
    def create(received_pattern):
        """Create a new pattern"""
        if not received_pattern:
            return

        new_pattern = Patterns(patternName=received_pattern.Name)

        db.session.add(new_pattern)
        db.session.commit()

        return new_pattern.id

    @staticmethod
    def pattern(pattern_id):
        """Get a specific pattern <pattern_id>"""
        ptn = Patterns.query.filter(Patterns.id == pattern_id).first()
        return ptn

    @staticmethod
    def update(pattern_id, received_pattern):
        """Update a specific pattern <pattern_id>"""
        if not received_pattern:
            return False

        ptn = Patterns.query.filter(Patterns.id == pattern_id).first()

        if ptn:
            ptn.patternName = getattr(received_pattern,'Name', ptn.patternName)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def delete(pattern_id):
        """Delete a specific patter <pattern_id>"""
        ptn = Patterns.query.filter(Patterns.id == pattern_id).first()

        if ptn:
            db.session.delete(ptn)
            db.session.commit()
            return True
        else:
            return False