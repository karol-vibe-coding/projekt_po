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
