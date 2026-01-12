from flask import Blueprint, current_app, jsonify, request

users_bp = Blueprint('users', __name__)


def get_storage():
    return current_app.config['STORAGE']


@users_bp.route('/users', methods=['GET'])
def get_users():
    storage = get_storage()
    users = storage.get_all()
    return jsonify(users), 200


@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    storage = get_storage()
    user = storage.get_by_id(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


@users_bp.route('/users', methods=['POST'])
def create_user():
    storage = get_storage()
    data = request.get_json()
    
    if not data or 'name' not in data or 'lastname' not in data:
        return jsonify({"error": "Invalid request body"}), 400
    
    user = storage.create(data['name'], data['lastname'])
    return jsonify(user), 201
