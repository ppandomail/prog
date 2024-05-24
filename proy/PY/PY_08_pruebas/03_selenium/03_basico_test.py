from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test:

    def test_no_results(self):
        driver = webdriver.Chrome()
        driver.get('http://www.automationpractice.pl/index.php')
        driver.find_element(By.ID, 'search_query_top').send_keys('Hola')
        driver.find_element(By.NAME, 'submit_search').click()
        time.sleep(10)
        actual = driver.find_element(By.XPATH, '//*[@id="center_column"]/p').text
        assert actual == 'No results were found for your search "Hola"'
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Women").click()
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT, "Dres").click()
        time.sleep(2)
        driver.close()
