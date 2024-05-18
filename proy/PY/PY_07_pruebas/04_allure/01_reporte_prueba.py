"""

Allure:

. Es un framework de reporte de prueba.

. Instalación de la aplicación de línea de comandos Allure
    sudo apt-add-repository ppa:qameta/allure
    sudo apt-get update
    sudo apt-get install allure

. Instalación manual: https://docs.qameta.io/allure/

. Instalación: pip install allure-pytest

. Ejecución: pytest --alluredir=./tmp ej500_allure_basico.py

"""

import pytest
import allure

@allure.step('Step with placeholders in the title, positional: "{0}", keyword: "{b}"')
def some_calculation(a, b):
    return a + b

@allure.title("This test has a custom title")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This description will be replaced at the end of the test.')
@allure.link('https://www.google.com')
def test_some_calculation_success():
    assert some_calculation(1, 2) == 3
    allure.dynamic.description('A final description.')

@allure.description('Description of test failure on some_calculator')
def test_some_calculation_failure():
    assert some_calculation(3, 4) == 8

@allure.description_html('<h1>Description html of test skip</h1>')
def test_skip():
    pytest.skip('for a reason!')

def test_broken():
    """Description docstring of test broken"""
    raise Exception('oops')
