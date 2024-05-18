"""

pytest:

. Es un framework de prueba unitario para Python. 
. Más simple de usar y eficiente que unittest.

. Instalación: pip install pytest
. Muestra versión               : pytest --version
. Funciones con test_* | *_test : pytest modulo.py
. La funcion test_xxx           : pytest modulo.py::test_xxx 
. Se ven los prints             : pytest -s  
. Muestra Ayuda                 : pytest -h

"""

# Ejemplo 1

def test_01():
    assert True

def test_02():
    assert False

def test_03():
    assert (1, 2, 3) == (1, 2, 3)


# Ejemplo 2

def increment_one(numero):
    return numero + 1

def test_increment():
    assert increment_one(1) == 2

# Ejemplo 3

def make_a_dict(a, b):
    operation = a + b
    return {'a': a, 'b': b, 'result': operation}

def test_make_a_dict():
    actual = make_a_dict(2, 3)
    expected = {'a': 2, 'b': 3, 'result': 5}
    assert actual == expected
