from models.functionalProcesses import  PatternFunctionalProcesses

'''Shared functions between modules //TODO : Transfert every functions here'''
class BusinessPatternFunctionalProcess(object):
    @staticmethod
    def get_functionalprocesses(pattern_id):
        return PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.pattern_id == pattern_id).all()

