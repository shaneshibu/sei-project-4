from app import db, ma
from models.base import BaseModel, BaseSchema

class Image(db.Model, BaseModel):

    __tablename__ = 'images'

    url = db.Column(db.Text, nullable=False)
    #user_id
    #post_ids

class ImageSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Image
