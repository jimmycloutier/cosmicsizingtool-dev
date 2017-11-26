from flask import jsonify, request, abort
from . import functionprocess
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
    fps = BusinessFunctionalProcess.all_db_functionalprocesses()
    all_fps = {'FunctionalProcesses' : [fp.to_json() for fp in fps]}
    return jsonify(all_fps)

@functionprocess.route("/v1.0/patternfuncprocs", methods=['GET'])
def get_all_patternfunctionalprocesses():
    """Get all functional processes related to pattern from database"""
    pfps = BusinessPatternFunctionalProcess.all_db_patternfunctionalprocesses()
    all_pfps = {'PatternFunctionalProcesses' : [pfp.to_json() for pfp in pfps]}
    return jsonify(all_pfps)

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses", methods=['GET'])
def get_functionalprocesses(organization_id, project_id):
    """Get all functional processes related to a specific project <project_id<"""
    fps = BusinessFunctionalProcess.functionalprocesses(organization_id,project_id)
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

    received_fp = json2obj(request.data)
    success =BusinessFunctionalProcess.create(organization_id, project_id, received_fp)

    if success:
        return jsonify({'message': 'New Functional Process created successfully.', 'ID': success}), 201
    else:
        abort(404)

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses", methods=['POST'])
def create_patternfunctionalprocesses(pattern_id):
    """Create a new functional process for a pattern <pattern_id> """

    if not request.json or not 'Name' in request.json:
        abort(400)

    received_fp = json2obj(request.data)
    success = BusinessPatternFunctionalProcess.create(pattern_id, received_fp)

    if success:
        return jsonify({'message': 'New Functional Process created successfully.', 'ID': success}), 201
    else:
        abort(404)

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>", methods=['GET'])
def get_this_functionalprocess(organization_id, project_id, fp_id):
    """Get a specific functional process <fp_id> """
    fp = BusinessFunctionalProcess.functionalprocess(organization_id, project_id, fp_id)
    return jsonify({'FunctionalProcesses': [fp.to_json()]} if fp else {'message': 'Functional Process not found'}), 404

@functionprocess.route("/v1.0/pattern/<pattern_id>/funcprocesses/<fp_id>", methods=['GET'])
def get_this_patternfunctionalprocess(pattern_id, fp_id):
    """Get a specific functional process <fp_id>(related to a Pattern)"""
    fp = BusinessPatternFunctionalProcess.functionalprocess(pattern_id, fp_id)
    return jsonify({'FunctionalProcesses': [fp.to_json()]} if fp else {'message': 'Functional Process not found'}), 404

@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>", methods=['PUT'])
def update_functionalprocess(organization_id, project_id, fp_id):
    """Update a specific functional process <fp_id>"""
    if not request.json:
        abort(400)

    received_fp = json2obj(request.data)
    success = BusinessFunctionalProcess.update(organization_id, project_id, fp_id, received_fp)

    if success:
        return jsonify({'message': 'Functional Process updated successfully'}), 202
    else:
        abort(404)

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>", methods=['PUT'])
def update_patternfunctionalprocess(pattern_id, fp_id):
    """Update a specific functional process <fp_id> (related to a pattern)"""
    if not request.json:
        abort(400)

    received_fp = json2obj(request.data)
    success = BusinessPatternFunctionalProcess.update(pattern_id, fp_id, received_fp)

    if success:
        return jsonify({'message': 'Functional Process updated successfully'}), 202
    else:
        abort(404)


@functionprocess.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>", methods=['DELETE'])
def delete_functionalprocess(organization_id, project_id, fp_id):
    """Delete a specific functional process <fp_id>"""
    success = BusinessFunctionalProcess.delete(organization_id, project_id, fp_id)

    if success:
        return jsonify({'message':'Functional Process deleted successfully'})
    else:
        return jsonify({'message':'Functional process not found'}), 400

@functionprocess.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>", methods=['DELETE'])
def delete_patternfunctionalprocess(project_id, fp_id):
    """Delete a specific functional process <fp_id> (related to a pattern)"""
    success = BusinessPatternFunctionalProcess.delete(project_id, fp_id)

    if success:
        return jsonify({'message':'Functional Process deleted successfully'})
    else:
        return jsonify({'message':'Functional process not found'}), 400



