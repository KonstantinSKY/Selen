import time
from faker import Faker
from random import randint
import unittest
from selenium.webdriver import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LetCodeTest(unittest.TestCase):

    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--start-maximized')
        opts.add_argument('--disable-extensions')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_add_person(self):
        driver = self.driver
        driver.get("http://99.153.249.66/admin/")
        driver.find_element(By.NAME, "username").send_keys("max")
        driver.find_element(By.NAME, "password").send_keys("MaxP!2023")
        driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "model-person").find_element(By.CLASS_NAME, "addlink").click()
        time.sleep(4)

        for n in range(100):
            print("Test :", n)
            self.fill_fields(driver)
            try:
                print("Test", n, "- passed")
            except Exception as e:
                print("Test", n, "- failed due to:", str(e))

    def fill_fields(self, driver):
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

        fields_data = {
            f_name: fake.first_name(),
            l_name: fake.last_name(),
            mid_name: fake.first_name(),
            birthday: fake.date_of_birth().strftime("%Y-%m-%d"),
            street: fake.street_address(),
            unit: fake.random_number(digits=3),
            city: fake.city(),
            state: fake.state(),
            zipcode: fake.postcode(),
            idNumber: fake.random_number(digits=8),
            idIssued: fake.past_date().strftime("%Y-%m-%d"),
            idExp: fake.future_date().strftime("%Y-%m-%d"),
            emergContact: fake.name()
        }

        for xpath, data in fields_data.items():
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.send_keys(data)
            time.sleep(1)

        Select(driver.find_element(By.ID, "id_sex")).select_by_index(randint(0, 2))
        driver.find_element(By.NAME, "_save").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "object-tools").find_element(By.CLASS_NAME, "addlink").click()

    def tearDown(self):
        self.driver.quit()
