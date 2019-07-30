from flask import Blueprint, request, g
from models.user import User, UserSchema
from lib.helpers import is_unique
from lib.secure_route import secure_route

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
    # errors = {}
    user, errors = user_schema.load(data)
    # check if username or email already exists
    for field in ('username', 'email'):
        if not is_unique(model=User, key=field, value=data.get(field)):
            username = field == 'username'
            errors[field] = 'That username is already taken' if username else 'That email already has an account'
    if errors:
        return errors, 422
    user.save()
    return user_schema.jsonify(user), 201

@api.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
    except:
        return {'message': 'That is not a valid JSON Object'}, 422
    # if post request does not include username or password fields return error
    for field in ('username', 'password'):
        if not field in data:
            required_field = 'Username or Email' if field == 'username' else 'Password'
            return {'message': f'{required_field} is required'}, 411
    # query by username column, if no user found then query by email column
    user = User.query.filter((User.username == data['username']) | (User.email == data['username'])).first()
    # if no user found or if password is incorrect return error
    if not user or not user.validate_password(data['password']):
        return {'message': 'Unauthorized'}, 401
    return {'message': f'Welcome Back {user.username}', 'token': user.generate_token()}, 202

@api.route('/users/<int:user_id>', methods=['GET'])
def show(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    return user_schema.jsonify(user), 200

@api.route('/profile', methods=['GET'])
@secure_route
def profile():
    return user_schema.jsonify(g.current_user), 200
