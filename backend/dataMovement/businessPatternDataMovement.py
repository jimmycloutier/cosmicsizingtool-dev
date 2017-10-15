from models.dataMovements import  PatternDataMovements

class BusinessPatternDataMovement(object):
    @staticmethod
    def get_datamovements(pattern_id, fp_ip):
        return PatternDataMovements.query.filter(PatternDataMovements.fp_id == fp_ip).all()