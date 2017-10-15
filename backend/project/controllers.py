import types
from flask import jsonify, request, abort, url_for
from . import project
from models.projects import  Projects
from models import db
from functionalProcess import BusinessPatternFunctionalProcess, BusinessFunctionalProcess
from dataMovement import BusinessPatternDataMovement


#Test API route
@project.route("/", methods=['GET'])
def test_project_route():
    return jsonify({'message': 'test project API'}), 201

@project.route("/v1.0/projects", methods=['GET'])
def get_all_projects():
    """Get all projects from database"""
    prjs = Projects.query.all()
    all_prjs = {'Projects' : [prj.to_json() for prj in prjs]}
    return jsonify(all_prjs)

@project.route("/v1.0/organizations/<organization_id>/projects", methods=['GET'])
def get_projects(organization_id):
    """Get all projects related to an organization <organization_id>"""
    prjs = Projects.query.filter(Projects.organization_id == organization_id).all()
    return jsonify({'Projects' : [prj.to_json() for prj in prjs]} if prjs else {'message': 'No projects found'}), 200 if prjs else 404


@project.route("/v1.0/organizations/<organization_id>/projects", methods=['POST'])
def create_project(organization_id):
    """Create a project related to an organization <organization_id>"""
    if not request.json or not 'Name' in request.json:
        abort(400)

    received_project = request.get_json()
    new_project = Projects(projectName=received_project['Name'], organization_id=organization_id)

    db.session.add(new_project)
    db.session.commit()

    return jsonify({'message': 'New Project created successfully'}), 201


@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>", methods=['GET'])
def get_this_project(organization_id, project_id):
    """Get a specific projet <project_id>"""
    prj = Projects.query.filter(Projects.id == project_id).first()
    return jsonify({'Projects': [prj.to_json()]} if prj else {'message': 'Project not found'}), 200 if prj else 404

@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>", methods=['PUT'])
def update_project(organization_id, project_id):
    """Update a specifif project <project_id>"""
    if not request.json:
        abort(400)

    prj = Projects.query.filter(Projects.id == project_id).first()

    if prj:
        prj.projectName = request.json.get('Name', prj.projectName)
        db.session.commit()

    return jsonify({'Projects': [prj.to_json()]} if prj else {'message': 'project not found'}), 200 if prj else 404


@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>", methods=['DELETE'])
def delete_project(organization_id, project_id):
    """Delete a specific project <project_id>"""
    prj = Projects.query.filter(Projects.id == project_id).first()

    if prj:
        db.session.delete(prj)
        db.session.commit()
        return jsonify({'message':'Project deleted successfully'}), 200
    else:
        return jsonify({'message':'Project not found'}), 400

@project.route("/v1.0/organizations/<organization_id>/projects/<project_id>/applypattern/<pattern_id>", methods=['GET'])
def apply_pattern(organization_id, project_id, pattern_id):
    """
    Apply a pattern to a projet
    JSON request can contain a list of datamovement names that need to be used for the project instead of the one
    specified in the pattern
    """
    fps = BusinessPatternFunctionalProcess.get_functionalprocesses(pattern_id)
    for fp in fps:
        fp_poco = fp.to_poco_obj()
        new_fpId = BusinessFunctionalProcess.create_functionalprocesses(organization_id, project_id, fp_poco)
        #dms = BusinessPatternDataMovement.get_datamovements(pattern_id, fp_ip)
        #for dm in dms:
            #Create dm to project (with rename)
            #break

    #all_fps = {'FunctionalProcesses-ApplyPattern' : [fp.to_json() for fp in fps]}
    all_fps = {'FunctionalProcesses-ApplyPattern' : new_fpId}
    return jsonify(all_fps)

