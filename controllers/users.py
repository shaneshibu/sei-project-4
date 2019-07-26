from flask import Blueprint
from models.user import User, UserSchema

api = Blueprint('users', __name__)

user_schema = UserSchema()

# index route for testing purposes
@api.route('/users', methods=['GET'])
def index():
    users = User.query.all()
    return user_schema.jsonify(users, many=True), 200
