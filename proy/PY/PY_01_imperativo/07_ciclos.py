"""

Tipos de bucles:

. Determinados (for ... in ...): se ejecutan un número determinado de veces. Se sabe a priori.
. Indeterminados (while): se ejecutan un número indeterminado de veces. No se sabe a priori y 
dependerá de las circunstancias durante la ejecución del programa.

"""
 
x = 0
while x < 3:
    print(x)
    x += 1

x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1

palabra = 'python'
for letra in palabra:
    print(letra)

for i in range(3):
    print(i)

for i in range(3):
    if i == 1:
        continue
    print(i)

for i in range(1, 10, 2):  # el 2 es un salto
    print(i, end=', ')