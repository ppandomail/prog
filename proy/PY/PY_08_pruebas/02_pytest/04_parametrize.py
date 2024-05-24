import pytest

"""

Parametrize:

. Ayuda a no repetir el codigo muchas veces

"""

# Ejemplo 1

@pytest.mark.parametrize('passwd', ['123456', 'abcdefdfs', 'as52345fasdf4'])
def test_password_length(passwd):
    assert len(passwd) >= 8

# Ejemplo 2

def some_calculation(a, b):
    return a + b

@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (3, 3, 6), (3, -2, 1)])
def test_some_calculation(a, b, expected):
    assert some_calculation(a, b) == expected
