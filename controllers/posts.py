from flask import Blueprint
from models.post import Post, PostSchema

api = Blueprint('posts', __name__)

post_schema = PostSchema()

@api.route('/posts', methods=['GET'])
def index():
    posts = Post.query.all()
    return post_schema.jsonify(posts, many=True), 200
