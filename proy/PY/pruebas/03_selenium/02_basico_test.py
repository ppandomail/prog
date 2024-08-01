from selenium import webdriver
from selenium.webdriver.common.by import By

class Test:

    def test_python_org_navigation_link(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")   
        self.driver.find_element(By.LINK_TEXT, "Docs").click()
        elem2 = self.driver.find_element(By.TAG_NAME, "h1")
        assert elem2.text == "Python 3.12.3 documentation"
        self.driver.close()

    def test_python_org_navigation_xpath(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
        self.driver.find_element(By.XPATH, "//*[@id='top']/nav/ul/li[3]/a").click()
        elem2 = self.driver.find_element(By.TAG_NAME, "h1")
        assert elem2.text == "Python 3.12.3 documentation"
        self.driver.close()
        

