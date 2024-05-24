"""

Fixtures: 

. Aayudan a no tener codigo duplicado.
. Seguimiento de la ejecución:  pytest --setup-show xxx.py

"""

import pytest

# Ejemplo 1

@pytest.fixture()
def db():
    print('Connection successful')
    yield
    print('Connection closed')

def search_user(user_id):
    d = {'001': 'ppando', '002': 'otrouser'}
    return d[user_id]

def test_search(db):
    assert search_user('001') == 'ppando'

def test_search2(db):
    assert search_user('002') == 'otrouser'


# Ejemplo 2

class Person:

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

def years_until_retirement(p):
    return p.age + 5

def name_and_age(p):
    return p.name, p.age

@pytest.fixture()
def person():
    return Person("foo", 30, "accountant")

def test_years_until_retirement(person):
    assert years_until_retirement(person) == 35

def test_name_and_age(person):
    assert name_and_age(person) == ("foo", 30)