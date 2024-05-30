import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola():
  return 'Hola Mundo'

@app.route('/chau')
def chau():
  return 'Chau Mundo'

@app.route('/fecha')
def fecha():
  fecha_actual = datetime.datetime.now()
  documento = """ <html>
                  <body>
                    <h2> Fecha y hora actual %s </h2>
                  </body>
                  </html> """ % fecha_actual
  return documento

# http://localhost:5000/bienvenido/pepe
@app.route('/bienvenido/<string:nombre>')
def bienvenido(nombre):
    return f'<h1>Bienvenido {nombre}</h1>'