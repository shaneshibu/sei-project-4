from datetime import datetime, timedelta
import jwt
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import validates_schema, ValidationError, fields, validate
from app import db, ma, bcrypt
from config.environment import secret
from .base import BaseModel, BaseSchema

class User(db.Model, BaseModel):

    __tablename__ = 'users'

    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, plaintext):
        self.password_hash = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def validate_password(self, plaintext):
        return bcrypt.check_password_hash(self.password_hash, plaintext)

    def generate_token(self):
        payload = {
            'iss': 'imagebored',
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': self.id
        }

        token = jwt.encode(payload, secret, 'HS256').decode('utf-8')
        return token

class UserSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = User
        exclude = ('password_hash',)
        load_only = ('password',)

    username = fields.String(
        required=True,
        validate=[
            validate.Length(min=4, max=30),
            validate.Regexp(regex=r'^[\w]+$', error='Letters, numbers, dashes, and underscores only. Please try again without symbols.')
            ]
        )
    email = fields.Email(required=True, validate=validate.Length(min=6, max=128))
    password = fields.String(required=True, validate=validate.Length(min=4, max=30))
    password_confirmation = fields.String(required=True)
    uploaded_images = fields.Nested('ImageSchema', many=True, only=('url'))
    created_posts = fields.Nested('PostSchema', many=True)

    @validates_schema
    # pylint: disable=R0201
    def check_passwords_match(self, data):
        if data.get('password') != data.get('password_confirmation'):
            raise ValidationError(
            'Passwords do not match.',
            'password_confirmation'
            )
