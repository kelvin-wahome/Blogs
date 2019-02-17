from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQlAlchemy()

def create_app(config_name):
    # Initialising application
    app = Flask (__name__)

    # Creating app configuration
    app.config.from_object(config_options[config_name])


    # Initializing Flask Extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
