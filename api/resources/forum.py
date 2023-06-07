from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api.schemas.forum import PostSchema
from models.forum import Post


class PostList(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        posts = Post.query.all()

        schema = PostSchema(many=True)

        return {"results": schema.dump(posts)}
