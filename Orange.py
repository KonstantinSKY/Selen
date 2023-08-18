import time
from faker import Faker
from random import randint
from unittest import TestCase
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC



class LetCodeTest(TestCase):

    def setUp(self):
        # opts = webdriver.FirefoxOptions()
        opts = webdriver.ChromeOptions()
        # opts.add_argument('--start-maximized')
        # opts.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_login_pos(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        assert driver.title == "OrangeHRM"
        print("Title is Correct. Current Title is:", driver.title)

    def test_login_neg(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin1235")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        a = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text
        print(a)
        assert driver.title == "OrangeHRM"
        print("Title is Correct. Current Title is:", driver.title)
        assert "Invalid credentials" == a
        print("Log in with invalid password OK")

    def test_add_employee(self):
        fake = Faker()
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        assert driver.title == "OrangeHRM"
        print("Title is Correct. Current Title is:", driver.title)
        f_name = "firstName"
        l_name  = "lastName"
        emp_id_xpath = "(//input[contains(@class,'oxd-input oxd-input--active')])[5]"
        save_class = "oxd-button--secondary"

        for i in range(20):
            driver.find_element(By.CLASS_NAME, "oxd-sidepanel").find_elements(By.TAG_NAME, "li")[1].click()
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "orangehrm-header-container").find_element(By.TAG_NAME, "button").click()

            time.sleep(2)
            driver.find_element(By.NAME, f_name).send_keys(fake.first_name())
            driver.find_element(By.NAME, l_name).send_keys(fake.last_name())
            a = driver.find_element(By.CLASS_NAME, "oxd-grid-2").find_element(By.TAG_NAME, "input")
            a.click()
            time.sleep(2)
            # a.clear()
            # time.sleep(2)
            a.send_keys(randint(0, 99999))
            driver.find_element(By.CLASS_NAME, save_class).click()
            time.sleep(4)
    def tearDown(self):
        self.driver.quit()
