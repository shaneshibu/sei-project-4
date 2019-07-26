from app import db, ma

class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    #user_id
    #post_ids

class ImageSchema(ma.ModelSchema):

    class Meta:
        model = Image
