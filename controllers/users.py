from flask import Blueprint, request
from models.user import User, UserSchema

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
    errors = {}
    user, errors = user_schema.load(data)
    if errors:
        return errors, 422
    user.save()
    return user_schema.jsonify(user), 200
