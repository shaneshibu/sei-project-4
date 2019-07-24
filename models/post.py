from app import db, ma
from models.base import BaseModel, BaseSchema

class Post(db.Model, BaseModel):

    __tablename__ = 'posts'

    title = db.Column(db.String(40), nullable=False)

class PostSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Post
