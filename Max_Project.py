import time
from faker import Faker
import unittest
import requests
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

faker_class = Faker()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--start-maximized')
        opts.add_argument('--disable-extensions')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def test_amazon_create_login(self):
        driver = self.driver
        driver.get("https://testpages.herokuapp.com/")
        driver.find_elements(By.ID, "jsattributes")
        for i in range(1, 99):
            elem = driver.find_elements(By.TAG_NAME, 'p')
        if elem.__getattribute__('nextid') == i:
            driver.find_elements(By.CLASS_NAME, "styled-click-button").click() #button

        # href_elements = self.driver.find_elements(By.TAG_NAME,"a")
        # for element in href_elements:
        #     print(element.text)
        #     print(element.get_attribute("href"))

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    # send keywordyds
    # for i in range(1, 100):
    #     element_par = (by TAG NAME, "p")
    #     element_par(be.css_selector, "p.nextid")
    #     if element_par.get_attribute(f'nextid')) == i":
    #         check...
    #     findelem(button).click()
    #     print(f'custom'-
    #     if element.get_attribute(f'custom-{i}')) == f"value_{i}"
    #         check
    #
