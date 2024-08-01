import pytest

# Se pone cualquier nombre de marca
# Ejemplo 1: Ejecución $pytest -m finished -vv

@pytest.mark.finished
def test_01():
    assert True

@pytest.mark.unfinished
def test_02():
    assert False

def test_03():
    assert (1, 2, 3) == (1, 2, 3)


# Ejemplo 2: Ejecución $pytest -m slow -vv
# Tambien se puede ejecutar $pytest -m "not slow" -vv
# Tambien se puede ejecutar $pytest -k calcul -vv      (tests cuyos nombres contienen calcul)

def some_calculation(a, b):
    return a + b

@pytest.mark.slow
def test_some_calculation():
    assert some_calculation(1, 2) == 3
