"""

Selenium:



. Doc: https://selenium-python.readthedocs.io/


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test:

    def test_search_in_python_org(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

# Se ejecuta con pytest
# /Users/ppando/Materias/.venv/bin/pytest /Users/ppando/Materias/prog/proy/PY/PY_08_pruebas/03_selenium/02_basico_test.py