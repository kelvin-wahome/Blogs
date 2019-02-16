from flask import Flask
from flask_bootstrap import Bootstrap

# Initialising application
app = Flask (__name__,instance_relative_config = True))

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
