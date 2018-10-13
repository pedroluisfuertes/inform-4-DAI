from flask import Flask
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

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404
