"""

Función filter:

. Función de orden superior (programación funcional)
. Verifica que los elementos de una secuencia cumplen una condición, devolviendo un iterador con los elementos que cumple dicha condición

"""

def par(n):
  return n % 2 == 0

numeros = [17, 24, 7, 39, 8, 51, 92]
lista = list(filter(par, numeros))
print(lista)

# Otra forma: con función lambda
numeros = [17, 24, 7, 39, 8, 51, 92]
lista = list(filter(lambda n : n % 2 == 0, numeros))
print(lista)
