from flask import jsonify, request, abort
from . import pattern
from .businessPattern import BusinessPattern
from utils import json2obj

#Test API
@pattern.route("/", methods=['GET'])
def test_pattern_route():
    return jsonify({'message': 'test'}), 201

@pattern.route("/v1.0/patterns", methods=['GET'])
def get_all_patterns():
    """Get all patterns from database"""
    ptns = BusinessPattern.all_db_patterns()
    all_ptns = {'Patterns' : [ptn.to_json() for ptn in ptns]}
    return jsonify(all_ptns)

@pattern.route("/v1.0/patterns/<pattern_id>", methods=['GET'])
def get_this_pattern(pattern_id):
    """Get a specific pattern <pattern_id>"""
    ptn = BusinessPattern.pattern(pattern_id)
    return jsonify({'Patterns': [ptn.to_json()]} if ptn else {'message': 'Pattern not found'}), 404

@pattern.route("/v1.0/patterns", methods=['POST'])
def create_pattern():
    """Create a new pattern"""
    if not request.json or not 'Name' in request.json:
        abort(400)

    received_pattern = json2obj(request.data)
    success = BusinessPattern.create(received_pattern)

    if success:
        return jsonify({'message':'New Pattern created successfully.', 'ID' : success }), 201
    else:
        abort(404)

@pattern.route("/v1.0/patterns/<pattern_id>", methods=['PUT'])
def update_pattern(pattern_id):
    """Update a specific pattern <pattern_id>"""
    if not request.json:
        abort(400)

    received_pattern = json2obj(request.data)
    success = BusinessPattern.update(received_pattern)

    if success:
        return jsonify({'message':'Pattern updated successfully.'}), 202
    else:
        abort(404)


@pattern.route("/v1.0/patterns/<pattern_id>", methods=['DELETE'])
def delete_pattern(pattern_id):
    """Delete a specific patter <pattern_id>"""
    success = BusinessPattern.delete(pattern_id)

    if success:
        return jsonify({'message': 'Pattern deleted successfully'})
    else:
        return jsonify({'message': 'Pattern not found'}), 400


