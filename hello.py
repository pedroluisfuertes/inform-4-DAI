from flask import Flask
try:
    from PIL import Image
except:
    import Image
from pintaMandelbrot import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user/pepe")
def usuaruioPepe():
    return "Hola Pepe"

@app.route("/user/<usuario>")
def todosLosUsuarios(usuario):
    return "Hola %s" %usuario

@app.route('/pintaMandelbrot')
def prog():   # los parámetros están en el request
    parametro1 = request.args.get('x1')   # hola
    parametro2 = request.args.get('y1')   # pepe
    parametro1 = request.args.get('x2')   # hola
    parametro2 = request.args.get('y2')   # pepe
    pintaMandelbrot(x1, y1, x2, y2, 400, 255, "pintaMandelbrotPic.jpg");
    response = Response()
    response.headers.add('Content-Type', 'image/png')
    imagen_jpg = Image.open("pintaMandelbrotPic.jpg");
    response.set_data(imagen_jpg)
    return response

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404
