"""

Función map:

. Función de orden superior
. Aplica una función a cada elemento de una lista iterable (listas, tuplas, etc.) 
  devolviendo una lista con los resultados.

"""

def cuadrado(n):
    return n * n

lista = list(map(cuadrado, [1, 2, 3]))
print(lista)
