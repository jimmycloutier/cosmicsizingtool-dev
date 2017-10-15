from flask import Blueprint

project= Blueprint('project', __name__, url_prefix='/prj')

from . import controllers
from .businessProject import BusinessProject