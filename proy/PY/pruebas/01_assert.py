"""

assert:

. Permite realizar comprobaciones (test unitarios)
. Si la expresión es False, se lanzará la excepción AssertionError

"""

def test_1igual1():
    print("Esto es una prueba")
    assert 1 == 1

test_1igual1()

def suma(a, b):
    return a + b

def test_suma():
    assert suma(1, 2) == 3

test_suma()