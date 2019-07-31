from flask import Blueprint, request, g
from models.post import Post, PostSchema, Entry
from models.image import Image
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
    if not data.entries in data and not data.entries:
        return {'message': 'Post does not contain any Entries'}, 422
    entries = []
    for entry in data.entries:
        entry_image = Image.query.get(entry.image_id)
        entry = Entry(image=entry_image, caption=entry.caption, pos=entry.pos)
        entries.append(entry)
    post_data = {'title': data.title, 'post_entries': entries}
    post, errors = post_schema.load(post_data)
    if errors:
        return errors, 422
    post.creator = g.current_user
    post.save()
    return post_schema.jsonify(post), 201

@api.route('/posts/<int:post_id>', methods=['GET'])
def show(post_id):
    post = Post.query.get(post_id)
    if not post:
        return {'message': 'Post not found'}, 404
    return post_schema.jsonify(post), 200

@api.route('/posts/<int:post_id>', methods=['PATCH'])
@secure_route
def update(post_id):
    post = Post.query.get(post_id)
    if not post:
        return {'message': 'Post not found'}, 404
    data = request.get_json()
    post, errors = post_schema.load(data, instance=post, partial=True)
    if errors:
        return errors, 422
    post.save()
    entries = Entry.query.filter_by(post_id=None).all()
    for entry in entries:
        entry.remove()
    return post_schema.jsonify(post), 200

@api.route('/posts/<int:post_id>', methods=['DELETE'])
@secure_route
def delete(post_id):
    post = Post.query.get(post_id)
    if not post:
        return {'message': 'Post not found'}, 404
    if post.creator != g.current_user:
        return {'message': 'Unauthorized'}, 401
    entries = Entry.query.filter_by(post_id=post.id).all()
    for entry in entries:
        entry.remove()
    post.remove()
    return {}, 204
