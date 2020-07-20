from flask import Flask
from flask_cors import CORS

import settings
from app import models
from app.api import api_bp
from app.frontend import main
from app.database import db, migrate


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(settings.Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(api_bp)
    app.register_blueprint(main)
    CORS(app, resourses={r"/*": {"origins": ["*"]}})


    return app
