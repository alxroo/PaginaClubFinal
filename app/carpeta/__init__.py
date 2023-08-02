from flask import Blueprint

carpeta = Blueprint('carpeta',__name__,template_folder='templates')

from . import views