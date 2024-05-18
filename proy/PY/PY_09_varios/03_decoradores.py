""""

Decoradores:

. Funciones que agregan funcionalidades a otras funciones.
. "Decoran" a otras funciones.
. Devuelve una función.

"""

def funcion_decorador(funcion):

  def funcion_interna():
    pass

  return funcion_interna


### Ejemplo sin parámetros

def funcion_decorador(funcion):

  def funcion_interna():
    print('->')
    funcion()
    print('<-')

  return funcion_interna

@funcion_decorador
def sumar():
  print(1 + 2)

sumar()

"""En consola:
->
3
<-
"""


### Ejemplo con parámetros

def funcion_decorador(funcion):

  def funcion_interna(*args):
    print('->')
    funcion(*args)
    print('<-')

  return funcion_interna

@funcion_decorador
def sumar(n1, n2):
  print(n1 + n2)

sumar(1, 2)
