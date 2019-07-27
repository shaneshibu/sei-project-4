from app import db, ma
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User

class Post(db.Model, BaseModel):

    __tablename__ = 'posts'

    title = db.Column(db.String(50), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', backref='posts')

class PostSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Post
