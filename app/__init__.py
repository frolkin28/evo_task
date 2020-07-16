from flask import Flask

import settings
from app.api import api_bp
from app.database import db


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(settings.Config)
    # db.init_app(app)
    app.register_blueprint(api_bp)

    return app
