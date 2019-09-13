from flask import Blueprint, request, jsonify
from flask.views import MethodView
from web.trees.helper import response
tree_mould = Blueprint('mould', __name__)


class TreeMolds(MethodView):

    def post(self):
        if request.content_type == 'application/json' or request.content_type == 'multipart/form-data':
            data = request.get_json()
            return jsonify(data)
        return response('failed', 'Content-type must be json', 400)


@tree_mould.route('/leaves')
def leaves():
    string = "<h1>This tree have leaves</h1>"
    return string


treeMould = TreeMolds.as_view('mould')

tree_mould.add_url_rule('/tree', view_func=treeMould, methods=['POST'])
