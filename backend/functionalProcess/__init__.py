from flask import Blueprint

functionprocess= Blueprint('functionalprocess', __name__, url_prefix='/fp')

from . import controllers