from app import db, ma

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)

class PostSchema(ma.ModelSchema):

    class Meta:
        model = Post
