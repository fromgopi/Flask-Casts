from flask import Blueprint
from flask_restful import Api

v1 = Blueprint('v1', __name__, url_prefix='/v1')

app = Api(v1)