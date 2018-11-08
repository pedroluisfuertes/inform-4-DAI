from flask import request # Para obtener los parámetros que te pasan por la url
from flask import Response #Para poder enviar imágenes 
from flask import Flask, render_template # Para renderizar plantillas, de jinja por ejemplo. 
from flask import session, redirect
import shelve
import math

app = Flask(__name__)
app.secret_key='Clave de sesión'

nPaginas = 0
def anadirPagina(pagina):
    global nPaginas
    
    if(nPaginas < 3):
        nPaginas = nPaginas + 1

    historial = [0]*(nPaginas + 1)
    if(nPaginas > 1):
        for i in range(nPaginas-1, 0, -1):
            aux1 = "histo" + str(i - 1)
            aux2 = "histo" + str(i)
            session[aux2] = session[aux1] 
            historial[i] = session[aux2]
            print(session[aux2])

    session["histo0"] = pagina
    historial[0] = pagina

    return historial

def mostrarPagina(pagina):
    if 'username' in session:
        user=session['username']#prácticas
        historial =  anadirPagina(pagina)
        return render_template(pagina,user = user, historial = historial)
        #return render_template('index.html',user = user)
    else :
        return render_template(pagina)

@app.route("/index.html")
@app.route("/index")
@app.route("/")
def index():
    return mostrarPagina("index.html")


@app.route("/surfbase.html")
@app.route("/surfbase")
def surfbase():
    return mostrarPagina("surfbase.html")
    

@app.route("/newsblog.html")
@app.route("/newsblog")
def newsblog():
    return mostrarPagina("newsblog.html")

@app.route("/about.html")
@app.route("/about")
def about():
    return mostrarPagina("about.html")

@app.route('/login.html',methods = ['POST','GET'])
@app.route('/login',methods = ['POST','GET'])
def login():
    
    #historial=aniadirHistorial("login")
    #comprobarCont()

    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        bd= shelve.open('datos.dat')
        
        if user in bd:
            datos = bd[user]
            if user == datos['user'] and passw == datos['pass']: 
                session['username']= user
                return render_template("usuario.html",user=user)
            else:
                return render_template('login.html', error = "Contraseña incorrecta")

            bd.close()

        else: 
            bd.close()
            return render_template('login.html', error = "Usuario no encontrado")
    else:
        if 'username' in session:
            username=session['username']
            
            return render_template('usuario.html', user=username,  historial=historial)
        else:
            return render_template('login.html')

@app.route("/usuario.html", methods = ['POST','GET'])
@app.route("/usuario", methods = ['POST','GET'])
def usuario():
    historial =  anadirPagina("index")
    if request.method == 'POST':
        user = request.form['user']
        session['username']=user
        datos = request.form
        bd= shelve.open('datos.dat')
        bd[user]=datos
        bd.close()
        return render_template("usuario.html", user=user, historial=historial)

    else:
        #return redirect(url_for('index'))
        return render_template('usuario.html')

@app.route('/logout.html')
@app.route('/logout')
def logout():
    historial =  anadirPagina("logout")
    
    session.pop('username', None)
    global nPaginas
    #for i in range(1, nPaginas):
        #ession.pop(i,None)
    if(nPaginas > 0):
        for i in range(0, nPaginas+1):
            aux1 = "histo" + str(i)
            session.pop(aux1, None)


    nPaginas = 0; 
    return render_template("logout.html")

@app.route('/datos.html', methods = ['POST','GET'])
@app.route('/datos', methods = ['POST','GET'])
def datos():
    historial=anadirPagina("datos.html")
    if request.method == 'POST':
        user = request.form['user']
        session['username']=user
        datos = request.form
        bd= shelve.open('datos.dat')
        bd[user]=datos
        bd.close()
        return render_template("datos.html", user=user, historial=historial, datos = datos)
    else:
        if 'username' in session:
            user=session['username']
            bd= shelve.open('datos.dat')
            datos= bd[user]
            bd.close()
            return render_template("datos.html", user=user, historial=historial, datos = datos)
        else: 
            return redirect(redirect('index'))

@app.errorhandler(404)
def page_not_found(error):
    return "Pagina no encontrada", 404

