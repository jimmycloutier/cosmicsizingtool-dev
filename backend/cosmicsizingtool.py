from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS

import os
os.environ['DEBUG'] = '1'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

cosmicsztool = Flask(__name__)
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