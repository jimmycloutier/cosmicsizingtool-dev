from flask import Blueprint

pattern= Blueprint('pattern', __name__, url_prefix='/ptn')

from . import controllers