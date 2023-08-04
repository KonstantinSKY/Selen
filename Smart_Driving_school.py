import time

from faker import Faker
from random import randint

import unittest

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import color
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

fake = Faker()

f_name = "//input[contains(@name,'first_name')]"
l_name = "//input[contains(@name,'last_name')]"
mid_name = "//input[contains(@name,'middle_name')]"
birthday = "//input[@type='text'][contains(@id,'birthday')]"
street = "//input[@type='text'][contains(@id,'address')]"
unit = "//input[@type='text'][contains(@id,'unit')]"
city = "//input[@type='text'][contains(@id,'city')]"
state = "//input[@type='text'][contains(@id,'state')]"
zipcode = "//input[@type='text'][contains(@id,'code')]"
idNumber = "//input[@type='text'][contains(@id,'number')]"
idIssued = "//input[contains(@name,'ID_issued_date')]"
idExp = "//input[contains(@name,'ID_expiration_date')]"
emergContact = "//input[@type='text'][contains(@id,'relationship')]"


class letcode_test(unittest.TestCase):

    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--start-maximized')
        opts.add_argument('--disable-extensions')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def fill_fields(self):
        driver = self.driver

        times = time.sleep
        fields_data = {
            f_name: fake.first_name(),
            l_name: fake.last_name(),
            mid_name: fake.first_name(),
            birthday: fake.date_of_birth(),
            street: fake.street_address(),
            unit: fake.random_number(digits=3),
            city: fake.city(),
            state: fake.state(),
            zipcode: fake.postcode(),
            idNumber: fake.random_number(digits=8),
            idIssued: fake.date_of_birth(),
            idExp: fake.date_of_birth(),
            emergContact: fake.name
        }

        for xpath, data in fields_data.items():
            driver.find_element("xpath", xpath).send_keys(data)
            times(1)
        for key in fields_data.keys():
            print(key)

        exit()

    def test_add_person(self):
        driver = self.driver
        times = time.sleep
        driver.get("http://99.153.249.66/admin/")
        driver.find_element(By.NAME, "username").send_keys("max")
        driver.find_element(By.NAME, "password").send_keys("MaxP!2023")
        driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
        times(3)
        driver.get(("http://99.153.249.66/admin/persons/person/add/"))
        # by(By.CLASS_NAME, "addlink").click() ##################################
        # Select(driver.find_element(By.ID, "id_sex")).select_by_index((randint(0, 2)))  ########################
        times(3)

        for n in range(100):
            print("Test :", n)
            try:
                self.fill_fields()
                print("Test", n, "- passed")
            except:
                print("Test", n, "- failed")

    def tearDown(self):
        self.driver.quit()
