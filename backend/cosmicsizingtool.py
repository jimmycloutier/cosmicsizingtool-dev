from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
from flasgger import Swagger

import os


cosmicsztool = Flask(__name__)
swagger = Swagger(cosmicsztool)
CORS(cosmicsztool)

cosmicsztool.config.from_object('config')

from models import db

db.init_app(cosmicsztool)
db.create_all(app=cosmicsztool)

from organization import organization
cosmicsztool.register_blueprint(organization)

from project import project
cosmicsztool.register_blueprint(project)

from pattern import pattern
cosmicsztool.register_blueprint(pattern)

from functionalProcess import functionprocess
cosmicsztool.register_blueprint(functionprocess)

from dataMovement import datamovement
cosmicsztool.register_blueprint(datamovement)

@cosmicsztool.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  cosmicsztool.run()