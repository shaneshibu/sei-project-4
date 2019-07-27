from flask import Blueprint, request, g
from models.image import Image, ImageSchema
from lib.secure_route import secure_route

api = Blueprint('images', __name__)

image_schema = ImageSchema()

@api.route('/images', methods=['GET'])
def index():
    images = Image.query.all()
    return image_schema.jsonify(images, many=True), 200

@api.route('/images', methods=['POST'])
@secure_route
def add():
    try:
        data = request.get_json()
    except:
        return {'message': 'That is not a valid JSON Object'}, 422
    image, errors = image_schema.load(data)
    if errors:
        return errors, 422
    image.uploader = g.current_user
    image.save()
    return image_schema.jsonify(image), 201

@api.route('/images/<int:image_id>', methods=['GET'])
def show(image_id):
    image = Image.query.get(image_id)
    if not image:
        return {'message': 'Image not found'}, 404
    return image_schema.jsonify(image), 200

@api.route('/images/<int:image_id>', methods=['DELETE'])
@secure_route
def delete(image_id):
    image = Image.query.get(image_id)
    if not image:
        return {'message': 'Image not found'}, 404
    if image.uploader != g.current_user:
        return {'message': 'Unauthorized'}, 401
    image.remove()
    return {}, 204
