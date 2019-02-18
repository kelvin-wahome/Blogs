from flask import Blueprint

auth = Blueprint('auth',__name___)

from . import views
