from marshmallow import fields
from app import db, ma
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User
# from .post import Entry

class Image(db.Model, BaseModel):

    __tablename__ = 'images'

    url = db.Column(db.Text, nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    uploader = db.relationship('User', backref='uploaded_images')
    height = db.Column(db.Integer, nullable=False, default=256)
    width = db.Column(db.Integer, nullable=False, default=256)
    # entries = db.relationship('Entry', backref='image_url')

class ImageSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Image
        exclude = ('updated_at',)

    posts = fields.Nested('EntrySchema', many=True, only='post')
    uploader = fields.Nested('UserSchema', only='username')
