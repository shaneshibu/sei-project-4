from flask import Blueprint, request, g
from models.post import Post, PostSchema
from lib.secure_route import secure_route

api = Blueprint('posts', __name__)

post_schema = PostSchema()

@api.route('/posts', methods=['GET'])
def index():
    posts = Post.query.all()
    return post_schema.jsonify(posts, many=True), 200

@api.route('/posts', methods=['POST'])
@secure_route
def create():
    try:
        data = request.get_json()
    except:
        return {'message': 'That is not a valid JSON Object'}, 422
    post, errors = post_schema.load(data)
    if errors:
        return errors, 422
    post.creator = g.current_user
    post.save()
    return post_schema.jsonify(post), 201
