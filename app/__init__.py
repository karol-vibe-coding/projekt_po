  from flask import Flask

from app.routes import users_bp
from app.storage import UserStorage


def create_app(storage=None):
    app = Flask(__name__)
    
    if storage is None:
        storage = UserStorage()
    
    app.config['STORAGE'] = storage
    app.register_blueprint(users_bp)
    
    return app
