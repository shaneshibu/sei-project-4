from app import db, ma
from models.base import BaseModel, BaseSchema
from models.post import Post

class Image(db.Model, BaseModel):

    __tablename__ = 'images'

    url = db.Column(db.Text, nullable=False)
    gif = db.Column(db.Boolean, default=False)
    caption = db.Column(db.String(100))
    #views
    #post_id
    #user_id

class ImageSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Image
