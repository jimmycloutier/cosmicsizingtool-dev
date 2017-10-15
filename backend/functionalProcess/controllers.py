from flask import jsonify, request, abort
from . import functionprocess
from models.functionalProcesses import  FunctionalProcesses, PatternFunctionalProcesses
from models import db
from .businessPatternFunctionalProcess import BusinessPatternFunctionalProcess
from .businessFunctionalProcess import BusinessFunctionalProcess
from utils import json2obj

#Test API
@functionprocess.route("/", methods=['GET'])
def test_fp_route():
    return jsonify({'message': 'test'}), 201

@functionprocess.route("/v1.0/funcprocs", methods=['GET'])
def get_all_functionalprocesses():
    """Get all functional processes from database"""
    fps = FunctionalProcesses.query.all()
    all_fps = {'FunctionalProcesses' : [fp.to_json() for fp in fps]}
    return jsonify(all_fps)

@functionprocess.route("/v1.0/patternfuncprocs", methods=['GET'])
def get_all_patternfunctionalprocesses():
    """Get all functional processes related to pattern from database"""
    pfps = PatternFunctionalProcesses.query.all()
    all_pfps = {'PatternFunctionalProcesses' : [pfp.to_json() for pfp in pfps]}
    return jsonify(all_pfps)

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses", methods=['GET'])
def get_functionalprocesses(organization_id, project_id):
    """Get all functional processes related to a specific project <project_id<"""
    fps = FunctionalProcesses.query.filter(FunctionalProcesses.project_id == project_id).all()
    all_fps = {'FunctionalProcesses' : [fp.to_json() for fp in fps]}
    return jsonify(all_fps)

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses", methods=['GET'])
def get_patternfunctionalprocesses(pattern_id):
    """Get all functional processes related to a specific pattern <pattern_id>"""
    fps = BusinessPatternFunctionalProcess.functionalprocesses(pattern_id)
    all_fps = {'FunctionalProcesses' : [fp.to_json() for fp in fps]}
    return jsonify(all_fps)

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses", methods=['POST'])
def create_functionalprocesses(organization_id, project_id):
    """Create a new functional process for a project <project_id>"""
    if not request.json or not 'Name' in request.json:
        abort(400)

    x = json2obj(request.data)
    new_id =BusinessFunctionalProcess.create(organization_id, project_id, x)

    return jsonify({'message': 'New Functional Process created successfully.', 'ID': new_id}), 201

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses", methods=['POST'])
def create_patternfunctionalprocesses(pattern_id):
    """Create a new functional process for a pattern <pattern_id> """
    if not request.json or not 'Name' in request.json:
        abort(400)

    received_fp = request.get_json()
    new_fp = PatternFunctionalProcesses(fpName=received_fp['Name'], pattern_id=pattern_id)

    db.session.add(new_fp)
    db.session.commit()

    return jsonify({'message': 'New Pattern Functional Process created successfully'}), 201

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>", methods=['GET'])
def get_this_functionalprocess(organization_id, project_id, fp_id):
    """Get a specific functional process <fp_id> """
    fp = FunctionalProcesses.query.filter(FunctionalProcesses.id == fp_id).first()
    return jsonify({'FunctionalProcesses': [fp.to_json()]} if fp else {'message': 'Functional Process not found'}), 404

@functionprocess.route("/v1.0/pattern/<pattern_id>/funcprocesses/<fp_id>", methods=['GET'])
def get_this_patternfunctionalprocess(pattern_id, fp_id):
    """Get a specific functional process <fp_id>(related to a Pattern)"""
    fp = PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.id == fp_id).first()
    return jsonify({'FunctionalProcesses': [fp.to_json()]} if fp else {'message': 'Functional Process not found'}), 404

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>", methods=['PUT'])
def update_functionalprocess(organization_id, project_id, fp_id):
    """Update a specific functional process <fp_id>"""
    if not request.json:
        abort(400)

    fp = FunctionalProcesses.query.filter(FunctionalProcesses.id == fp_id).first()

    if fp:
        fp.fpName = request.json.get('Name', fp.fpName)
        db.session.commit()

    return jsonify({'Functional Processes': [fp.to_json()]} if fp else {'message': 'Function Process not found'}), 404

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>", methods=['PUT'])
def update_patternfunctionalprocess(pattern_id, fp_id):
    """Update a specific functional process <fp_id> (related to a pattern)"""
    if not request.json:
        abort(400)

    fp = PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.id == fp_id).first()

    if fp:
        fp.fpName = request.json.get('Name', fp.fpName)
        db.session.commit()

    return jsonify({'Functional Processes': [fp.to_json()]} if fp else {'message': 'Function Process not found'}), 404


@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>", methods=['DELETE'])
def delete_functionalprocess(organization_id, project_id, fp_id):
    """Delete a specific functional process <fp_id>"""
    fp = FunctionalProcesses.query.filter(FunctionalProcesses.id == fp_id).first()

    if fp:
        db.session.delete(fp)
        db.session.commit()
        return jsonify({'message':'Functional Process deleted successfully'})
    else:
        return jsonify({'message':'Functional process not found'}), 400

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>", methods=['DELETE'])
def delete_patternfunctionalprocess(project_id, fp_id):
    """Delete a specific functional process <fp_id> (related to a pattern)"""
    fp = PatternFunctionalProcesses.query.filter(PatternFunctionalProcesses.id == fp_id).first()

    if fp:
        db.session.delete(fp)
        db.session.commit()
        return jsonify({'message':'Functional Process deleted successfully'})
    else:
        return jsonify({'message':'Functional process not found'}), 400



