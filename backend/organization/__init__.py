from flask import Blueprint

organization= Blueprint('organization', __name__, url_prefix='/org')

from . import controllers
