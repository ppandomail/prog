from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hola')
def hola():
    return render_template('hola.html')

@app.route('/chau')
def chau():
    return render_template('chau.html', nom='Mundo')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])   # Por default es 'GET'
def contacto():
    nombre = request.form.get('nombre')     # 'nombre' es el valor del attr 'name' del input
    return render_template('contacto.html', nombre=nombre)