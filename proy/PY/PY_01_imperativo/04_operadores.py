"""

Operadores:

. aritméticos = {+, -, *, /, //, %, **}
. relacionales = {==, !=, >, >=, <, <=}
. lógicos = {and, or, not}
. asignación = {=, +=, -=, *=, /=, %=, **=, //=}
. especiales = {is, is not, in, in not}

"""

a = 3
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # cociente division entera
print(a % b)
print(a ** b)  # potencia

a += 1
print(a)
a -= 1
print(a)

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

b1 = True   # asociado el valor 1
b2 = False  # asociado el valor 0

print(b1)
print(b2)

# Operaciones con booleanos
print(b1 == b2)
print(b1 != b2)
print(b1 > b2)
print(b1 >= b2)
print(b1 < b2)
print(b1 <= b2)

print(not b1)
print(b1 and b2)
print(b1 or b2)
