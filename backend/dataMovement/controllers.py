from flask import jsonify, request, abort
from . import datamovement
from models.dataMovements import  DataMovements, PatternDataMovements
from models import db
from . import datamove_func
from .businessPatternDataMovement import BusinessPatternDataMovement

#test route
@datamovement.route("/", methods=['GET'])
def test_dm_route():
        return jsonify({'message': 'test'}), 201

@datamovement.route("/v1.0/datamoves", methods=['GET'])
def get_all_datamovements():
    """Get all datamovements from database """
    dms = DataMovements.query.all()
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/patterndatamoves", methods=['GET'])
def get_all_patterndatamovements():
    """Get all datamovements related to a pattern from database"""
    pdms = PatternDataMovements.query.all()
    all_pdms = {'PatternDataMovements': [pdm.to_json() for pdm in pdms]}
    return jsonify(all_pdms)

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_ip>/datamoves", methods=['GET'])
def get_datamovements(organization_id, project_id, fp_id):
    """Get all datamovements for a specific functional process <fp_id>"""
    dms = DataMovements.query.filter(DataMovements.fp_id == fp_id).all()
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_ip>/datamoves", methods=['GET'])
def get_patterndatamovements(pattern_id, fp_ip):
    """Get all datamovements for a specific functional process (related to a pattern) <fp_id>"""
    dms = BusinessPatternDataMovement.get_datamovements(pattern_id, fp_ip)
    all_dms = {'DataMovements' : [dm.to_json() for dm in dms]}
    return jsonify(all_dms)

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocsses/<fp_ip>/datamoves", methods=['POST'])
def create_datamovements(organization_id, project_id, fp_id):
    """Create new datamovement for a specific functional process <fp_id>"""
    if not request.json or not 'Name' in request.json or 'Move' in request.json :
        abort(400)

    received_dm = request.get_json()
    move = received_dm['Move'].upper()
    if not datamove_func.isValidMove(move):
        abort(400)

    new_dm = DataMovements(dmName=received_dm['Name'], move=move, fp_id=fp_id)

    db.session.add(new_dm)
    db.session.commit()

    return jsonify({'message': 'New Data movements created successfully'}), 201

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_ip>/datamoves", methods=['POST'])
def create_patterndatamovements(pattern_id, fp_id):
    """Create new datamovement for a specific functional process (realted to a pattern) <fp_id>"""
    if not request.json or not 'Name' in request.json or 'Move' in request.json :
        abort(400)

    received_dm = request.get_json()
    move = received_dm['Move']
    move = move.upper()
    if not datamove_func.isValidMove(move):
        abort(400)

    received_dm = request.get_json()
    new_dm = PatternDataMovements(dmName=received_dm['Name'], move=move, fp_id=fp_id)

    db.session.add(new_dm)
    db.session.commit()

    return jsonify({'message': 'New Data movements created successfully'}), 201

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['GET'])
def get_this_datamovement(organization_id, project_id, fp_id, dm_id):
    """Get a specific datamovement <dm_id>"""
    dm = DataMovements.query.filter(DataMovements.id == dm_id).first()
    return jsonify({'DateMovements': [dm.to_json()]} if dm else {'message': 'Data Movements not found'}), 404

@datamovement.route("/v1.0/pattern/<pattern_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['GET'])
def get_this_patterndatamovement(pattern_id, fp_id, dm_id):
    """Get a specific datamovement (related to a pattern) <dm_id>"""
    dm = PatternDataMovements.query.filter(PatternDataMovements.id == dm_id).first()
    return jsonify({'DataMovements': [dm.to_json()]} if dm else {'message': 'Data Movement not found'}), 404

@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['PUT'])
def update_datamovement(organization_id, project_id, fp_id, dm_id):
    """Update a specific datamovement <dm_id>"""
    if not request.json:
        abort(400)

    dm = DataMovements.query.filter(DataMovements.id == dm_id).first()

    if dm:
        dm.dmName = request.json.get('Name', dm.dmName)

        move = request.json.get('Move', dm.movement)
        if move:
            move = move.upper()
            if not datamove_func.isValidMove(move):
                abort(400)
            else:
                dm.movement = request.json.get('Move', dm.movement)

        db.session.commit()

    return jsonify({'DataMovements': [dm.to_json()]} if dm else {'message': 'Data Movement not found'}), 404

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['PUT'])
def update_patterndatamovement(pattern_id, fp_id, dm_id):
    """Update a specific datamovement (related to a pattern) <dm_id>"""
    if not request.json:
        abort(400)

    dm = PatternDataMovements.query.filter(PatternDataMovements.id == dm_id).first()

    if dm:
        dm.dmName = request.json.get('Name', dm.dmName)

        move = request.json.get('Move', dm.movement)
        if move:
            move = move.upper()
            if not datamove_func.isValidMove(move):
                abort(400)
            else:
                dm.movement = request.json.get('Move', dm.movement)

        db.session.commit()

    return jsonify({'DataMovements': [dm.to_json()]} if dm else {'message': 'Data Movement not found'}), 404


@datamovement.route("/v1.0/organizations/<organization_id>/projects/<project_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['DELETE'])
def delete_datamovement(organization_id, project_id, fp_id, dm_id):
    """Delete a specific data movement <dm_id>"""
    dm = DataMovements.query.filter(DataMovements.id == dm_id).first()

    if dm:
        db.session.delete(dm)
        db.session.commit()
        return jsonify({'message':'Data Movement deleted successfully'})
    else:
        return jsonify({'message':'Data Movement not found'}), 400

@datamovement.route("/v1.0/patterns/<pattern_id>/funcprocesses/<fp_id>/datamoves/<dm_id>", methods=['DELETE'])
def delete_patterndatamovement(project_id, fp_id, dm_id):
    """Delete a specific data movement (related to a pattern) <dm_id>"""
    dm = PatternDataMovements.query.filter(PatternDataMovements.id == dm_id).first()

    if dm:
        db.session.delete(dm)
        db.session.commit()
        return jsonify({'message':'Data Movement deleted successfully'})
    else:
        return jsonify({'message':'Data Movement not found'}), 400



