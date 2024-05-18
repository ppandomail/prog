"""

Listas:

. Estructura de datos que nos permiten almacenar gran cantidad de valores.
. Pueden guardar distintos tipos de valores.
. Se pueden expandir dinámicamente, agregando nuevos elementos.

"""

lista_vacia = []
lista = ['Maria', 'Pepe', 'Marta', 'Antonio']
lista_lista = [1, [2, 3], 4]

# list(c): crea una lista con los elementos de la secuencia o colección c.
print(list())
print(list((1, 2, 3)))
print(list('python'))

lista[:]   # Toda la lista
lista[2]   # Marta
lista[7]   # IndexError: list index out of range
lista[-2]  # Marta
lista[0:3] # ['Maria', 'Pepe', 'Marta']
lista[1:]  # ['Pepe', 'Marta', 'Antonio']
lista[:2]  # ['Maria', 'Pepe']

# operaciones que no modifican la lista
len(lista) # 4
min(lista)
max(lista)
sum(lista)
lista.index('Antonio')  # 3
lista.count('Antonio')  # 1
'Pepe' in lista         # True
'Juan' in lista         # False

# Operaciones que modifican la lista
lista.append('Ana')             # agrega al final
lista.insert(2, 'Ana')          # agrega en índice 2
lista.extend(['Luis', 'Pablo']) # une listas al final
lista.remove('Ana')
lista.pop()                     # elimina último elemento
lista.sort()
lista.reverse()

# Listas por comprensión
lista = [1, 2, 3, 4, 5, 6]
[x*2 for x in lista if x > 2]
