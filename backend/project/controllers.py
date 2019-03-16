import types
from flask import jsonify, request, abort, url_for
from . import project
from .businessProject import BusinessProject
from utils import json2obj, json2dict


#Test API route
@project.route("/", methods=['GET'])
def test_project_route():
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    return jsonify({'message': 'test project API'}), 201

@project.route("/v1.0/projects", methods=['GET'])
def get_all_projects():
    """Get all projects from database
        This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    prjs = BusinessProject.all_db_projects()
    all_prjs = {'Projects' : [prj.to_json() for prj in prjs]}
    return jsonify(all_prjs)

@project.route("/v1.0/organizations/<organization_id>/projects", methods=['GET'])
def get_projects(organization_id):
    """Get all projects related to an organization <organization_id>"""
    prjs = BusinessProject.projects(organization_id)
    return jsonify({'Projects' : [prj.to_json() for prj in prjs]} if prjs else {'message': 'No projects found'}), 200 if prjs else 404

@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>", methods=['GET'])
def get_this_project(organization_id, project_id):
    """Get a specific projet <project_id>"""
    prj = BusinessProject.project(organization_id, project_id)
    return jsonify({'Projects': [prj.to_json()]} if prj else {'message': 'Project not found'}), 200 if prj else 404

@project.route("/v1.0/organizations/<organization_id>/projects", methods=['POST'])
def create_project(organization_id):
    """Create a project related to an organization <organization_id>"""
    if not request.json or not 'Name' in request.json:
        abort(400)
    print(request.json)
    received_project = json2obj(request.data)
    success = BusinessProject.create(organization_id, received_project)

    if success:
        return jsonify({'message':'New Project created successfully.', 'ID' : success }), 201
    else:
        abort(404)

@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>", methods=['PUT'])
def update_project(organization_id, project_id):
    """Update a specifif project <project_id>"""
    if not request.json:
        abort(400)

    received_project = json2obj(request.data)
    success = BusinessProject.update(organization_id, project_id,received_project)

    if success:
        return jsonify({'message':'Project updated successfully.'}), 202
    else:
        abort(404)


@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>", methods=['DELETE'])
def delete_project(organization_id, project_id):
    """Delete a specific project <project_id>"""
    success = BusinessProject.delete(organization_id, project_id)

    if success:
        return jsonify({'message':'Project deleted successfully'}), 200
    else:
        return jsonify({'message':'Project not found'}), 400

@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>/applypattern/<pattern_id>", methods=['GET', 'PATCH'])
def apply_pattern(organization_id, project_id, pattern_id):
    """
    Apply a pattern to a projet
    JSON request can contain a list of datamovement names that need to be used for the project instead of the one
    specified in the pattern
    """

    if request.json:
        received_renameList = json2dict(request.data)
    else:
        received_renameList = {}

    print(received_renameList)
    success = BusinessProject.apply_pattern(organization_id,project_id, pattern_id,received_renameList )

    if success:
        return jsonify({'message':'Pattern applied successfully to project'}), 200
    else:
        return jsonify({'message':'Pattern not applied. Error'}), 400

