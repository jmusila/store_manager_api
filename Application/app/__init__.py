from flask import Flask
from .api.v1.views import api
from instance.config import app_config
from flask_jwt_extended import JWTManager


def create_app(config_name):
    app = Flask(__name__)
    app.url_map.strict_slashes=False
    app.config.from_object(app_config[config_name])
    api.init_app(app)

    return app