from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api.schemas.forum import PostSchema
from auth.decorators import auth_role
from models.forum import Post


class PostList(Resource):
    method_decorators = [auth_role("admin"), jwt_required()]

    def get(self):
        posts = Post.query.all()

        schema = PostSchema(many=True)

        return {"results": schema.dump(posts)}
