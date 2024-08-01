"""

Función reduce:

. Operar todos elementos de una colección iterable (reduce)
. reduce(f, l): aplicar la función f a los dos primeros elementos de la secuencia l.
. Con ese valor vuelve aplicar con el siguiente.

"""

from functools import reduce

def producto(n, m):
    return n * m

resultado = reduce(producto, range(1, 5))
print(resultado)
