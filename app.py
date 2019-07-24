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
post_schema = PostSchema()

@app.route('/posts')
def index():
    posts = Post.query.all()
    return post_schema.jsonify(posts, many=True), 200
