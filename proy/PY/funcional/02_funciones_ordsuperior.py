"""

Funciones de orden superior:

. En python las funciones pueden pasarse como argumentos de una función

"""

def aplica(f, arg):
    return f(arg)

def cuadrado(n):
    return n * n

def cubo(n):
    return n**3

print(aplica(cuadrado, 5))
print(aplica(cubo, 5))