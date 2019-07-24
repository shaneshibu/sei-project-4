from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.environment import db_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# pylint: disable=C0413
from models.post import Post, PostSchema
from models.image import Image, ImageSchema
post_schema = PostSchema()
image_schema = ImageSchema()

@app.route('/posts')
def posts_index():
    posts = Post.query.all()
    return post_schema.jsonify(posts, many=True), 200

@app.route('/images')
def images_index():
    images = Image.query.all()
    return image_schema.jsonify(images, many=True), 200
