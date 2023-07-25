import time
from faker import Faker
from random import randint
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
from selenium.webdriver.support.ui import Select

faker_class = Faker()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--start-maximized')
        opts.add_argument('--disable-extensions')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_amazon_create_login(self):
        driver = self.driver
        driver.get("https://testpages.herokuapp.com/styled/attributes-test.html")
        # elem = driver.find_element(By.ID, "jsattributes")

        for i in range(1, 5):

            elem = driver.find_element(By.ID, "jsattributes")

            if elem.get_attribute('nextid') == str(i):
                print("OK")
            else:
                print("NOT OK nextid different ", i)
            driver.find_element(By.CLASS_NAME, "styled-click-button").click()  # button
            if elem.get_attribute("custom-" + str(i)) == ("value-" + str(i)):
                print("OK value")
            else:
                print("Not OK value is", i)

    def test_Basic_HTML_Form_Example(self):
        print("Second test")
        driver = self.driver
        driver.get("https://testpages.herokuapp.com/")
        driver.find_element(By.ID, "htmlformtest").click()
        check_box_random = randint(0, 2)
        driver.find_elements(By.NAME, "radioval")[randint(0, 2)].click()
        driver.find_elements(By.NAME, "checkboxes[]")[check_box_random].click()
        time.sleep(5)

        # select = Select(driver.find_element(By.NAME, 'dropdown'))
        # select.select_by_index(randint(0, 5))
        Select(driver.find_element(By.NAME, 'dropdown')).select_by_index(randint(0, 5))
        # select.select_by_visible_text("Drop Down Item 1")
        # select.select_by_value(value)
        Select(driver.find_element(By.NAME, "multipleselect[]")).select_by_index(randint(0, 3))

        driver.find_elements(By.NAME, "submitbutton")[1].click()
        time.sleep(5)
        submit_form = driver.find_element(By.ID, "_valuecheckboxes0").text

        if "cb" + str(check_box_random + 1) == submit_form:
            print("Form OK")
        else:
            print("Form Bad")

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
    # href_elements = self.driver.find_elements(By.TAG_NAME,"a")
    # for element in href_elements:
    #     print(element.text)
    #     print(element.get_attribute("href"))
