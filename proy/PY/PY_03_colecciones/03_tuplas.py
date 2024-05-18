"""

Tuplas:

. Son listas inmutables (no se pueden modificar después de su creación)
. Ventajas:
  . Más rápidas en cuanto a ejecución
  . Menos espacio (mayor optimización)
  . Pueden usarse como claves en un diccionario (las listas no)

"""

tupla_vacia = ()
tupla = ('Juan', 13, 1, 1995)
tupla_tupla = ((1, 2, 3), (4, 5, 6))

# tuple(c): crea una tupla con los elementos de la secuencia o colección c.
print(tuple())
print(tuple([1, 2, 3]))
print(tuple('python'))

tupla[1]             # 13
len(tupla)           # 4
tupla.count(9)       # 1
tupla.index('Juan')  # 0
'Juan' in tupla      # True

list(tupla)          # Convierte tupla en lista
tuple([1, 2])        # Convierte lista en tupla

nom, dd, mm, yyyy = tupla # desempaquetado de tupla
print(nom)                # 'Juan'
