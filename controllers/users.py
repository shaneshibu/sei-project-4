from flask import Blueprint, request
from models.user import User, UserSchema
from lib.helpers import is_unique

api = Blueprint('users', __name__)

user_schema = UserSchema()

# index route for testing purposes
@api.route('/users', methods=['GET'])
def index():
    users = User.query.all()
    return user_schema.jsonify(users, many=True), 200

@api.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
    except:
        return {'message': 'That is not a valid JSON Object'}, 422
    user, errors = user_schema.load(data)
    # check if username or email already exists
    for field in ('username', 'email'):
        if not is_unique(model=User, key=field, value=data.get(field)):
            username = field == 'username'
            errors[field] = 'That username is already taken' if username else 'That email already has an account'
    if errors:
        return errors, 422
    user.save()
    return user_schema.jsonify(user), 200
