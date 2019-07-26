from flask import Blueprint
from models.image import Image, ImageSchema

api = Blueprint('images', __name__)

image_schema = ImageSchema()

@api.route('/images', methods=['GET'])
def index():
    images = Image.query.all()
    return image_schema.jsonify(images, many=True), 200
