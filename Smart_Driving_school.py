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

    def test_add_person(self):
        driver = self.driver
        driver.get("http://99.153.249.66/admin/")
        driver.find_element(By.NAME, "username").send_keys("max")
        driver.find_element(By.NAME, "password").send_keys("MaxP!2023")
        driver.find_element(By.CLASS_NAME, "submit-row").find_element(By.TAG_NAME, "input").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "model-person").find_element(By.CLASS_NAME, "addlink").click()

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
        zipcode = "//input[@type='text'][contains(@id,'code')]"
        idNumber = "//input[@type='text'][contains(@id,'number')]"
        idIssued = "//input[contains(@name,'ID_issued_date')]"
        idExp = "//input[contains(@name,'ID_expiration_date')]"
        emergContact = "//input[@type='text'][contains(@id,'relationship')]"

        fields_data = {
            f_name: fake.first_name(),
            l_name: fake.last_name(),
            mid_name: fake.first_name(),
            birthday: fake.date_of_birth(minimum_age=10, maximum_age=130).strftime("%Y-%m-%d"),
            street: fake.street_address(),
            unit: fake.random_number(digits=3),
            city: fake.city(),
            zipcode: fake.postcode(),
            idNumber: fake.random_number(digits=8),
            idIssued: fake.past_date().strftime("%Y-%m-%d"),
            idExp: fake.future_date().strftime("%Y-%m-%d"),
            emergContact: fake.name()
        }

        for xpath, data in fields_data.items():
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.send_keys(data)
            time.sleep(1)
        time.sleep(2)
        Select(driver.find_element(By.ID, "id_sex")).select_by_value(str(randint(0, 2)))
        time.sleep(2)
        Select(driver.find_element(By.ID, "id_ID_state")).select_by_value(str(randint(7, 15)))
        Select(driver.find_element(By.NAME, "state")).select_by_value(str(randint(7, 15)))

        driver.find_element(By.NAME, "_save").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "object-tools").find_element(By.CLASS_NAME, "addlink").click()
        time.sleep(2)

    def state_fill(self):
        fake = Faker()
        driver = self.driver
        driver.get("http://99.153.249.66/admin/")
        driver.find_element(By.NAME, "username").send_keys("max")
        driver.find_element(By.NAME, "password").send_keys("MaxP!2023")
        driver.find_element(By.CLASS_NAME, "submit-row").find_element(By.TAG_NAME, "input").click()
        time.sleep(2)
        # driver.find_element(By.CLASS_NAME, "model-state").find_elements(By.TAG_NAME, "th")[0].click()
        driver.find_element(By.XPATH, "//a[contains(.,'States')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//a[contains(.,"Add state")]').click()
        postal = "//input[@id='id_postal_name']"
        state = "//input[@id='id_name']"

        add_state = {
            postal: fake.state_abbr(),
            state: fake.state()
        }
        for xpath, data in add_state.items():
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.send_keys(data)
            time.sleep(1)

        Select(driver.find_element(By.ID, "id_time_zone")).select_by_value(str(randint(0, 5)))
        driver.find_element(By.NAME, "_save").click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//a[contains(.,"Add state")]').click()
        time.sleep(5)

    def test_state(self):

        for n in range(100):
            self.state_fill()

        time.sleep(5)

    def test_fill_correct_states(self):

        states_info = {
            "AL": ("Alabama", "Central (CT)"),
            "AK": ("Alaska", "Alaska (AKT)"),
            "AZ": ("Arizona", "Mountain (MT)"),
            "AR": ("Arkansas", "Central (CT)"),
            "CA": ("California", "Pacific (PT)"),
            "CO": ("Colorado", "Mountain (MT)"),
            "CT": ("Connecticut", "Eastern (ET)"),
            "DE": ("Delaware", "Eastern (ET)"),
            "FL": ("Florida", "Eastern (ET)"),
            "GA": ("Georgia", "Eastern (ET)"),
            "HI": ("Hawaii", "Hawaii-Aleutian (HST)"),
            "ID": ("Idaho", "Mountain (MT)"),
            "IL": ("Illinois", "Central (CT)"),
            "IN": ("Indiana", "Eastern (ET)"),
            "IA": ("Iowa", "Central (CT)"),
            "KS": ("Kansas", "Central (CT)"),
            "KY": ("Kentucky", "Eastern (ET)"),
            "LA": ("Louisiana", "Central (CT)"),
            "ME": ("Maine", "Eastern (ET)"),
            "MD": ("Maryland", "Eastern (ET)"),
            "MA": ("Massachusetts", "Eastern (ET)"),
            "MI": ("Michigan", "Eastern (ET)"),
            "MN": ("Minnesota", "Central (CT)"),
            "MS": ("Mississippi", "Central (CT)"),
            "MO": ("Missouri", "Central (CT)"),
            "MT": ("Montana", "Mountain (MT)"),
            "NE": ("Nebraska", "Central (CT)"),
            "NV": ("Nevada", "Pacific (PT)"),
            "NH": ("New Hampshire", "Eastern (ET)"),
            "NJ": ("New Jersey", "Eastern (ET)"),
            "NM": ("New Mexico", "Mountain (MT)"),
            "NY": ("New York", "Eastern (ET)"),
            "NC": ("North Carolina", "Eastern (ET)"),
            "ND": ("North Dakota", "Central (CT)"),
            "OH": ("Ohio", "Eastern (ET)"),
            "OK": ("Oklahoma", "Central (CT)"),
            "OR": ("Oregon", "Pacific (PT)"),
            "PA": ("Pennsylvania", "Eastern (ET)"),
            "RI": ("Rhode Island", "Eastern (ET)"),
            "SC": ("South Carolina", "Eastern (ET)"),
            "SD": ("South Dakota", "Central (CT)"),
            "TN": ("Tennessee", "Central (CT)"),
            "TX": ("Texas", "Central (CT)"),
            "UT": ("Utah", "Mountain (MT)"),
            "VT": ("Vermont", "Eastern (ET)"),
            "VA": ("Virginia", "Eastern (ET)"),
            "WA": ("Washington", "Pacific (PT)"),
            "WV": ("West Virginia", "Eastern (ET)"),
            "WI": ("Wisconsin", "Central (CT)"),
            "WY": ("Wyoming", "Mountain (MT)")
        }

        driver = self.driver
        driver.get("http://99.153.249.66/admin/")
        driver.find_element(By.NAME, "username").send_keys("max")
        driver.find_element(By.NAME, "password").send_keys("MaxP!2023")
        driver.find_element(By.CLASS_NAME, "submit-row").find_element(By.TAG_NAME, "input").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "model-state").find_elements(By.TAG_NAME, "th")[0].click()
        driver.find_element(By.XPATH, "//a[contains(.,'States')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//a[contains(.,"Add state")]').click()
        time.sleep(5)
        postal = "//input[@id='id_postal_name']"
        state = "//input[@id='id_name']"
        Select(driver.find_element(By.ID, "id_time_zone")).select_by_value(str(randint(0, 5)))

        for _ in range(100):
            for PN, state_info in states_info.items():
                driver.find_element(By.XPATH, postal).send_keys(PN)
                driver.find_element(By.XPATH, state).send_keys(state_info[0])
                Select(driver.find_element(By.ID, "id_time_zone")).select_by_visible_text(state_info[1])
                time.sleep(5)
                driver.find_element(By.NAME, "_save").click()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "object-tools").find_element(By.CLASS_NAME, "addlink").click()
                time.sleep(5)

    def tearDown(self):
        self.driver.quit()
