"""

Excepciones:

. Error en tiempo de ejecución
. La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado"
. Este tipo de errores de ejecución se pueden controlar para que la ejecución del programa continúe. Es lo que se conoce como manejo o control de excepciones.
. Tipos:
  . TypeError
  . ValueError
  . ZeroDivisionError
  . OverflowError
  . IndexError -> Acceder a secuencia con index inexistente
  . KeyError -> Acceder a dict con key inexistente
  . FileNotFoundError -> Acceder a archivo inexistente
  . ImportError -> Falla importación módulo

"""

# try - except
def divide(n1, n2):
  try:
    return n1 / n2
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
    return 'operación errónea'

# Mecanismo de reanudación
while True:
  try:
    n1 = int(input('Num 1: '))
    n2 = int(input('Num 2: '))
    break
  except ValueError:
    print('Valores incorrectos. Intente nuevamente')
print(divide(n1, n2))      

# try - 2 except
def divide():
  try:
    n1 = int(input('Num 1: '))
    n2 = int(input('Num 2: '))
    print('La división es ' + str(n1 / n2))
  except ValueError:
    print('Valores incorrectos')
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
  print('Cálculo finalizado')

divide()


# Lanzamiento de excepciones: raise
def evalua_edad(edad):
  if edad < 0:
    raise TypeError('No se permiten edades negativas')


import math
def calcular_raiz(num):
  if num < 0:
    raise ValueError('No puede ser negativo')
  else:
    return math.sqrt(num)

n = int(input('Número: '))
try:
  print(calcular_raiz(n))
except ValueError as ErrorNumNeg:
  print(ErrorNumNeg)

