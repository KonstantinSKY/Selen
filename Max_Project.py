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
        driver = self.driver
        driver.get("https://testpages.herokuapp.com/")
        driver.find_element(By.ID, "htmlformtest").click() #next page HTML Form Example
        check_box_random = randint(0, 2)
        driver.find_elements(By.NAME, "radioval")[randint(0, 2)].click() # click random radio every time

        driver.find_elements(By.NAME, "checkboxes[]")[check_box_random].click() # click random checkbox every time
        time.sleep(5)

        Select(driver.find_element(By.NAME, 'dropdown')).select_by_index(randint(0, 5)) #choosing random dropdown by Select
        Select(driver.find_element(By.NAME, "multipleselect[]")).select_by_index(randint(0, 3))#Multiple Select Values

        driver.find_elements(By.NAME, "submitbutton")[1].click()
        time.sleep(5)
        #checking if random checkbox have same value with submited form
        submit_form = driver.find_element(By.ID, "_valuecheckboxes0").text

        if "cb" + str(check_box_random + 1) == submit_form:
            print("Form OK")
        else:
            print("Form Bad")

        time.sleep(10)
    def test_Dynamic_HTML_TABLE_Tag(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        driver.get("https://testpages.herokuapp.com/")
        driver.find_element(By.ID, "dynamictablestest").click()  # next page Dynamic Table Test Page
        time.sleep(5)
        # checking if title is correct
        try:
            assert driver.title == "Table HTML Tag - JavaScript Created"
            print("Title is Correct. Current Title is:", driver.title)

        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

    # checking if current urs is CORRECT
        acct_reg_expected_url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
        acct_reg_actual_url = driver.current_url
        if acct_reg_expected_url == acct_reg_actual_url:
            print('"Account registration" page URL is correct:', driver.current_url)
        else:
            print('"Account registration" page URL is wrong:', driver.current_url)
        #     #check if header h1 text is correct
        # text_website = driver.find_elements(By.XPATH, "//h1[contains(.,'Dynamic HTML TABLE Tag')]").text
        # text_expected = "Dynamic HTML TABLE Tag"
        # if text_website == text_expected:
        #     try:
        #         assert text_website == text_expected
        #         print("Paragraph text is correct. Current text is:", text_website)
        #     except AssertionError:
        #         print("Paragraph text is different. Current text is:", text_website)
        driver.find_element(By.TAG_NAME, "p") # checking first paragraph
        driver.find_element(By.ID, "refreshtable") # refresh table button
        driver.find_element(By.ID, "caption") # placeholder Caption
        driver.find_element(By.ID, "tableid") # placeholder Id
        #driver.find_elements(By.TAG_NAME, "a") как найти все href в теге а


    def tearDown(self):
        self.driver.quit()
