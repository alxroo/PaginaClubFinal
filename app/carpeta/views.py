from . import carpeta
from ..models import Blog,Notice

@carpeta.route('/prueba')
def prueba():
    return "HOLA MUNDO"

@carpeta.route('/generateFakes')
def generateFakes():
    Blog.generate_fake_one(10)
    Notice.generate_fake_one(10)

    return "LISTO"