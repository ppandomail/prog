"""

Funciones lambda:

. Función anónima (sin nombre)
. Se usa para abreviar
. Nunca tendrá condicionales ni bucles

"""

# Función tradicional
def area(b, h):
  return (b * h)/2

print(area(5, 7))

# Funciones lambda
area = lambda b, h : (b * h) / 2
print(area(5, 7)) 

cubo = lambda n : pow(n, 3)
print(cubo(2))
