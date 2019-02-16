from flask import Flask
from app import views
from app import error
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    # Initialising application
    app = Flask (__name__)

    # Creating app configuration
    app.config.from_object(config_options[config_name])


    # Initializing Flask Extensions
    bootstrap.init_app(app)
    return app
