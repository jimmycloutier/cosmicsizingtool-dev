from flask import jsonify, request, abort
from . import datamovement
from .businessPatternDataMovement import BusinessPatternDataMovement
from .businessDataMovement import BusinessDataMovement
from utils import json2obj

#test route
@datamovement.route("/", methods=['GET'])
def test_dm_route():
        return jsonify({'message': 'test'}), 201

@datamovement.route("/v1.0/datamoves", methods=['GET'])
def get_all_datamovements():
    """Get all datamovements from database """
    dms = BusinessDataMovement.all_db_datamovements()
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/patterndatamoves", methods=['GET'])
def get_all_patterndatamovements():
    """Get all datamovements related to a pattern from database"""
    pdms = BusinessPatternDataMovement.all_db_datamovements()
    all_pdms = {'PatternDataMovements': [pdm.to_json() for pdm in pdms]}
    return jsonify(all_pdms)






@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/datamoves", methods=['GET'])
def get_datamovements_specific_project(organization_id, project_id):
    """Get all datamovements for a specific project <project_id>"""
    dms = BusinessDataMovement.datamovements_specific_project(organization_id, project_id)
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/patterns/<pattern_id>/datamoves", methods=['GET'])
def get_patterndatamovements_specific_pattern(pattern_id):
    """Get all datamovements for a specific patterns <pattern_id>"""
    dms = BusinessPatternDataMovement.datamovements_specific_pattern(pattern_id)
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)





@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves", methods=['GET'])
def get_datamovements(organization_id, project_id, fp_id):
    """Get all datamovements for a specific functional process <fp_id>"""
    dms = BusinessDataMovement.datamovements(organization_id, project_id, fp_id)
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>/datamoves", methods=['GET'])
def get_patterndatamovements(pattern_id, fp_id):
    """Get all datamovements for a specific functional process (related to a pattern) <fp_id>"""
    dms = BusinessPatternDataMovement.datamovements(pattern_id, fp_id)
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves", methods=['POST'])
def create_datamovements(organization_id, project_id, fp_id):
    """Create new datamovement for a specific functional process <fp_id>"""
    if not request.json or not 'Name' in request.json or not 'Move' in request.json :
        abort(400)

    received_dm = json2obj(request.data)
    success = BusinessDataMovement.create(organization_id, project_id, fp_id, received_dm)
    if success:
        return jsonify({'message': 'New Data movements created successfully', 'ID' : success}), 201
    else:
        abort(400)

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>/datamoves", methods=['POST'])
def create_patterndatamovements(pattern_id, fp_id):
    """Create new datamovement for a specific functional process (realted to a pattern) <fp_id>"""
    if not request.json or not 'Name' in request.json or 'Move' in request.json :
        abort(400)

    received_dm = json2obj(request.data)
    success = BusinessPatternDataMovement.create(pattern_id,fp_id, received_dm)
    if success:
        return jsonify({'message': 'New Data movements created successfully', 'ID' : success}), 201
    else:
        abort(404)

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['GET'])
def get_this_datamovement(organization_id, project_id, fp_id, dm_id):
    """Get a specific datamovement <dm_id>"""
    dm = BusinessDataMovement.datamovement(organization_id, project_id, fp_id, dm_id)
    return jsonify({'DateMovements': [dm.to_json()]} if dm else {'message': 'Data Movements not found'}), 404

@datamovement.route("/v1.0/pattern/<pattern_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['GET'])
def get_this_patterndatamovement(pattern_id, fp_id, dm_id):
    """Get a specific datamovement (related to a pattern) <dm_id>"""
    dm = BusinessPatternDataMovement.datamovement(pattern_id,fp_id, dm_id)
    return jsonify({'DataMovements': [dm.to_json()]} if dm else {'message': 'Data Movement not found'}), 404

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['PUT'])
def update_datamovement(organization_id, project_id, fp_id, dm_id):
    """Update a specific datamovement <dm_id>"""
    print(request.json)
    if not request.json:
        abort(400)
    received_dm = json2obj(request.data)
    success = BusinessDataMovement.update(organization_id,project_id, fp_id, dm_id, received_dm)
    if success:
        return jsonify({'message': 'Data Movement updated successfully'}), 202
    else:
        abort(404)

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['PUT'])
def update_patterndatamovement(pattern_id, fp_id, dm_id):
    """Update a specific datamovement (related to a pattern) <dm_id>"""
    if not request.json:
        abort(400)

    received_dm = json2obj(request.data)
    success = BusinessPatternDataMovement.update(pattern_id, fp_id, dm_id, received_dm)

    if success:
        return jsonify({'message': 'Data Movement updated successfully'}), 202
    else:
        abort(404)


@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['DELETE'])
def delete_datamovement(organization_id, project_id, fp_id, dm_id):
    """Delete a specific data movement <dm_id>"""
    success = BusinessDataMovement.delete(organization_id,project_id,fp_id,dm_id)

    if success:
        return jsonify({'message':'Data Movement deleted successfully'}), 200
    else:
        abort(404)

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['DELETE'])
def delete_patterndatamovement(project_id, fp_id, dm_id):
    """Delete a specific data movement (related to a pattern) <dm_id>"""
    success = BusinessPatternDataMovement.delete(project_id,fp_id,dm_id)

    if success:
        return jsonify({'message':'Data Movement deleted successfully'}), 200
    else:
        abort(404)


