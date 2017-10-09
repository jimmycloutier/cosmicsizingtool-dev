from flask import render_template, jsonify, flash, make_response, request, abort
from . import organization
from models.organizations import Organizations
from models import db

@organization.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@organization.route("/v1.0/organizations", methods=['GET'])
def get_all_organizations():
    """Get all organizations from database"""
    orgs = Organizations.query.all()
    all_orgs = {'Organizations': [org.to_json() for org in orgs]}
    return jsonify(all_orgs)

@organization.route("/v1.0/organizations", methods=['POST'])
def create_organization():
    """Create a new organization"""
    if not request.json or not 'Name' in request.json:
        abort(400)

    received_organization = request.get_json()

    new_organization = Organizations(organizationName=received_organization['Name'], organizationURL=received_organization.get('URL', "www"))

    db.session.add(new_organization)
    db.session.commit()

    return jsonify({'message': 'New Organization created successfully'}), 201

@organization.route("/v1.0/organizations/<organization_id>", methods=['GET'])
def get_an_organization(organization_id):
    """Get a specific organization <organization_id>"""
    org = Organizations.query.filter(Organizations.id == organization_id).first()
    return jsonify({'Organizations': [org.to_json()]} if org else {'message': 'organization not found'}), 404

@organization.route("/v1.0/organizations/<organization_id>", methods=['PUT'])
def update_organization(organization_id):
    """Update a specific organization"""
    if not request.json:
        abort(400)

    org = Organizations.query.filter(Organizations.id == organization_id).first()

    if org:
        org.organizationName = request.json.get('Name', org.organizationName)
        org.organizationURL = request.json.get('URL', org.organizationURL)
        db.session.commit()

    return jsonify({'Organizations': [org.to_json()]} if org else {'message': 'organization not found'}), 404

@organization.route("/v1.0/organizations/<organization_id>", methods=['DELETE'])
def delete_organization(organization_id):
    """Delete a specific organization <organization_id>"""
    org = Organizations.query.filter(Organizations.id == organization_id).first()

    if org:
        db.session.delete(org)
        db.session.commit()
        return jsonify({'message': 'Organization deleted successfully'})
    else:
        return jsonify({'message': 'Organization not found'}), 400
