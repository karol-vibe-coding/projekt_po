from flask import Blueprint, current_app, jsonify, request

users_bp = Blueprint('users', __name__)


def get_storage():
    return current_app.config['STORAGE']


@users_bp.route('/users', methods=['GET'])
def get_users():
    storage = get_storage()
    users = storage.get_all()
    return jsonify(users), 200
