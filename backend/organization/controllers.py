from flask import render_template, jsonify, flash, make_response, request, abort
from . import organization
from .businessOrganization import BusinessOrganization
from utils import json2obj

@organization.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@organization.route("/v1.0/organizations", methods=['GET'])
def get_all_organizations():
    """Get all organizations from database"""
    orgs = BusinessOrganization.organizations()
    all_orgs = {'Organizations': [org.to_json() for org in orgs]}
    return jsonify(all_orgs)

@organization.route("/v1.0/organizations/<organization_id>", methods=['GET'])
def get_an_organization(organization_id):
    """Get a specific organization <organization_id>"""
    org = BusinessOrganization.organization(organization_id)
    return jsonify({'Organizations': [org.to_json()]} if org else {'message': 'organization not found'}), 404

@organization.route("/v1.0/organizations", methods=['POST'])
def create_organization():
    """Create a new organization"""
    if not request.json or not 'Name' in request.json:
        abort(400)

    received_organization = json2obj(request.data)
    success = BusinessOrganization.create(received_organization)

    if success:
        return jsonify({'message':'New Organization created successfully.', 'ID' : success }), 201
    else:
        abort(404)

@organization.route("/v1.0/organizations/<organization_id>", methods=['PUT'])
def update_organization(organization_id):
    """Update a specific organization"""
    if not request.json:
        abort(400)

    received_organization = json2obj(request.data)
    success = BusinessOrganization.update(received_organization)

    if success:
        return jsonify({'message':'Organization updated successfully.'}), 202
    else:
        abort(404)

@organization.route("/v1.0/organizations/<organization_id>", methods=['DELETE'])
def delete_organization(organization_id):
    """Delete a specific organization <organization_id>"""
    success = BusinessOrganization.delete(organization_id)

    if success:
        return jsonify({'message': 'Organization deleted successfully'})
    else:
        return jsonify({'message': 'Organization not found'}), 400
