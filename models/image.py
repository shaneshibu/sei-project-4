from sqlalchemy.orm import backref
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

    #post_ids

class ImageSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Image

    image_entries = fields.Nested('EntrySchema', many=True)
