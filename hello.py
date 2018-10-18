from flask import Flask
try:
    from PIL import Image
except:
    import Image

from mandelbrot import *
from flask import request # Para obtener los parámetros que te pasan por la url
from flask import Response #Para poder enviar imágenes 
from flask import Flask, render_template # Para renderizar plantillas, de jinja por ejemplo. 

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
def pintaMandelbrot():   # los parometros estan en el request
    x1 = float(request.args.get('x1'))
    y1 = float(request.args.get('y1'))
    x2 = float(request.args.get('x2'))
    y2 = float(request.args.get('y2'))

    paleta = [[255,    0,   0], 
              [0,    255,   0], 
              [0,      0, 255]];

    renderizaMandelbrotBonito(x1, y1, x2, y2, 400, 255, "templates/pintaMandelbrotPic.png", paleta, 3 );
    imagen_png = Image.open("templates/pintaMandelbrotPic.png")
    response = Response()
    response.headers.add('Content-Type', 'image/png')
    response.set_data(imagen_png)   # Datos binarios
    return response

    #return render_template('fractal.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Pagina no encontrada", 404
