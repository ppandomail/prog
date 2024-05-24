"""

Pytest-mock:

. Es una libreria que permite mockear (engañar), sin ejecutar el código de la función.
. Instalación: pip install pytest-mock

"""

def some_calculation(a, b):
    return a + b

def test_some_calculation():
    assert some_calculation(1, 2) == 3

def make_a_dict(a, b):
    operation = some_calculation(a, b)
    return {"a": a, "b": b, "result": operation}

def test_make_a_dict(mocker):
    mocker.patch("06_mock.some_calculation", return_value=5, autospec=True)
    actual = make_a_dict(2, 3)
    expected = {"a": 2, "b": 3, "result": 5}
    assert actual == expected
