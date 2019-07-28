from marshmallow import fields
from app import db, ma
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User
from .image import Image

class Post(db.Model, BaseModel):

    __tablename__ = 'posts'

    title = db.Column(db.String(50), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', backref='created_posts')

class PostSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Post

    # images = fields.Nested('ImageSchema', many=True, only=('url'))
    post_entries = fields.Nested('EntrySchema', many=True, exclude=('created_at', 'updated_at', 'id'))

class Entry(db.Model, BaseModel):

    __tablename__ = 'entries'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    position = db.Column(db.Integer, default=0)
    caption = db.Column(db.String(30))
    post = db.relationship('Post', backref='post_entries')
    image = db.relationship('Image', backref='image_entries')

class EntrySchema(ma.ModelSchema):

    class Meta:
        model = Entry
