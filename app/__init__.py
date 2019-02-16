from flask import Flask
from app import views
from app import error
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


# Initialising application
app = Flask (__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
