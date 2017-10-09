from flask import jsonify, request, abort
from . import pattern
from models.patterns import  Patterns
from models import db

#Test API
@pattern.route("/", methods=['GET'])
def test_pattern_route():
    return jsonify({'message': 'test'}), 201

@pattern.route("/v1.0/patterns", methods=['GET'])
def get_all_patterns():
    """Get all patterns from database"""
    ptns = Patterns.query.all()
    all_ptns = {'Patterns' : [ptn.to_json() for ptn in ptns]}
    return jsonify(all_ptns)

@pattern.route("/v1.0/patterns", methods=['POST'])
def create_pattern():
    """Create a new pattern"""
    if not request.json or not 'Name' in request.json:
        abort(400)

    received_pattern = request.get_json()
    new_pattern = Patterns(patternName=received_pattern['Name'])

    db.session.add(new_pattern)
    db.session.commit()

    return jsonify({'message': 'New pattern created successfully'}), 201


@pattern.route("/v1.0/patterns/<pattern_id>", methods=['GET'])
def get_this_pattern(pattern_id):
    """Get a specific pattern <pattern_id>"""
    ptn = Patterns.query.filter(Patterns.id == pattern_id).first()
    return jsonify({'Patterns': [ptn.to_json()]} if ptn else {'message': 'Pattern not found'}), 404

@pattern.route("/v1.0/patterns/<pattern_id>", methods=['PUT'])
def update_pattern(pattern_id):
    """Update a specific pattern <pattern_id>"""
    if not request.json:
        abort(400)

    ptn = Patterns.query.filter(Patterns.id == pattern_id).first()

    if ptn:
        ptn.patternName = request.json.get('Name', ptn.patternName)
        db.session.commit()

    return jsonify({'Patterns': [ptn.to_json()]} if ptn else {'message': 'pattern not found'}), 404


@pattern.route("/v1.0/patterns/<pattern_id>", methods=['DELETE'])
def delete_pattern(pattern_id):
    """Delete a specific patter <pattern_id>"""
    ptn = Patterns.query.filter(Patterns.id == pattern_id).first()

    if ptn:
        db.session.delete(ptn)
        db.session.commit()
        return jsonify({'message':'Pattern deleted successfully'})
    else:
        return jsonify({'message':'Pattern not found'}), 400


