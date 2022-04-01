from flask import Flask
from flask_bootstrap import Bootstrap

from src.config import Config
from src.auth.app import auth


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app
