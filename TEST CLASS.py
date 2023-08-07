from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

fake = Faker()


class letcode_test(unittest.TestCase):

    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--start-maximized')
        opts.add_argument('--disable-extensions')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_add_person(self):
        driver = self.driver
        times = time.sleep
        driver.get("http://99.153.249.66/admin/")
        driver.find_element(By.NAME, "username").send_keys("max")
        driver.find_element(By.NAME, "password").send_keys("MaxP!2023")
        driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
        times(3)
        driver.find_element(By.CLASS_NAME, "model-person").find_element(By.CLASS_NAME, "addlink").click()
        times(4)

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
            birthday: fake.date_of_birth(),
            street: fake.street_address(),
            unit: fake.random_number(digits=3),
            city: fake.city(),
            state: fake.state(),
            zipcode: fake.postcode(),
            idNumber: fake.random_number(digits=8),
            idIssued: fake.date_of_birth(),
            idExp: fake.date_of_birth(),
            emergContact: fake.name()
        }

        for xpath, data in fields_data.items():
            print(xpath, data)
            print(driver.find_element(By.XPATH, xpath))
            driver.find_element(By.XPATH, xpath).send_keys(data)
            times(1)
        Select(driver.find_element(By.ID, "id_sex")).select_by_index(randint(0, 2))

        exit()

        for n in range(5):
          print("Test :", n)
        test_add_person()
        try:

            print("Test", n, "- passed")
        except:
            print("Test", n, "- failed")

    def tearDown(self):
        self.driver.quit()
