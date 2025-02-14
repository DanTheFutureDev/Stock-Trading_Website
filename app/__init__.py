from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db
from .routes import main
import logging

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(main)
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Enable SQLAlchemy logging
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    
    return app