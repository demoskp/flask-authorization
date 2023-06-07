from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from api.resources.forum import PostList

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(PostList, "/posts")


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
