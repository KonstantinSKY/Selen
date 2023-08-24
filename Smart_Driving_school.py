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

fake = Faker()


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

    def test_pos_reg(self):
        driver = self.driver
        driver.get("http://99.153.249.66/")
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, "btn-outline-warning")[1].click()

        time.sleep(1)

        names_list = [
            "Eloise O'Reilly", "Leandre D'Amico", "Chloe D'Angelo", "Zoe O'Connell", "Celeste O'Malley",
            "Leo O'Leary", "Theodore D'Souza", "Anais O'Mara", "Ismael D'Costa", "Maelys O'Sullivan",
            "Noemie O'Malley", "Celine D'Arcy", "Nehemie O'Neal", "Cedric O'Dwyer", "Oceane D'Lorenzo",
            "Leonard D'Amore", "Zoe O'Brian", "Celia D'Agostino", "Matheo O'Callaghan", "Maelle O'Grady",
            "Theophile D'Angelo", "Lea O'Malley", "Raphael D'Costa", "Melodie O'Reilly", "Hugo D'Amico",
            "Lena O'Sullivan", "Nicolas O'Dwyer", "Leandro D'Souza", "Sarah O'Neal", "Baptiste O'Leary",
            "Ines D'Lorenzo", "Maxime D'Arcy", "Isabelle O'Mara", "Octave O'Connell", "Clara O'Brian",
            "Timeo O'Reilly", "Manon O'Leary", "Robin D'Amico", "Leo O'Neal", "Valentin O'Dwyer",
            "Margaux D'Costa", "Nathan O'Connell", "Oceane D'Souza", "Melina O'Malley", "Lucas O'Leary",
            "Roxane D'Arcy", "Gabriel O'Dwyer", "Emma D'Lorenzo", "Cedric O'Reilly", "Zoe O'Mara",
            "Leon D'Angelo", "Manon D'Amico", "Simon O'Sullivan", "Juliette D'Costa", "Ethan O'Connell",
            "Clemence O'Neal", "Maxence D'Souza", "Leane O'Reilly", "Antoine D'Amico", "Camille O'Dwyer",
            "Jules D'Lorenzo", "Raphael D'Souza", "Lena O'Malley", "Leo O'Reilly", "Margaux D'Arcy",
            "Theo O'Connell", "Emma O'Leary", "Alexandre D'Angelo", "Lena O'Mara", "Clement O'Dwyer",
            "Lucas D'Amico", "Manon D'Costa", "Hugo O'Connell", "Lou D'Souza", "Romain O'Neal",
            "Chloe D'Lorenzo", "Lea O'Dwyer", "Baptiste D'Angelo", "Oceane O'Reilly", "Raphael O'Connell",
            "Mathilde D'Amico", "Victor D'Souza", "Leonie D'Costa", "Noe O'Neal", "Maelle O'Leary",
            "Theo O'Dwyer", "Leon D'Lorenzo", "Juliette D'Angelo", "Jules O'Connell", "Lea O'Neal",
            "Maxime O'Dwyer", "Hugo D'Amore", "Lou D'Souza", "Manon D'Costa", "Leo O'Connell",
            "Celeste O'Neal", "Raphael D'Lorenzo", "Oceane D'Amico", "Lucas D'Arcy", "Chloe D'Souza"
        ]

        positive_emails = [
            "john.doe@example.com", "jane.smith@example.com", "alex.wilson@example.com",
            "emily.jones@example.com", "michael.brown@example.com", "sarah.johnson@example.com",
            "david.jackson@example.com", "olivia.miller@example.com", "james.davis@example.com",
            "emma.anderson@example.com", "william.thomas@example.com", "ava.white@example.com",
            "charles.robinson@example.com", "sophia.clark@example.com", "joseph.harris@example.com",
            "mia.lewis@example.com", "george.lee@example.com", "abigail.hall@example.com",
            "samuel.green@example.com", "isabella.turner@example.com", "ethan.carter@example.com",
            "oliver.phillips@example.com", "ava.roberts@example.com", "amelia.baker@example.com",
            "benjamin.walker@example.com", "emily.cook@example.com", "jacob.campbell@example.com",
            "chloe.kelly@example.com", "mason.morgan@example.com", "sophia.james@example.com",
            "daniel.hughes@example.com", "mia.price@example.com", "william.evans@example.com",
            "olivia.richardson@example.com", "alexander.cooper@example.com", "ava.bell@example.com",
            "michael.collins@example.com", "amelia.cook@example.com", "david.murphy@example.com",
            "emma.bailey@example.com", "james.stewart@example.com", "isabella.brown@example.com",
            "jackson.jenkins@example.com", "sophia.wood@example.com", "oliver.parker@example.com",
            "mia.ward@example.com", "ethan.martin@example.com", "lily.harris@example.com",
            "noah.mitchell@example.com", "ava.morris@example.com", "william.roberts@example.com",
            "olivia.campbell@example.com", "daniel.phillips@example.com", "sophia.king@example.com",
            "logan.anderson@example.com", "isabella.hall@example.com", "jackson.adams@example.com",
            "amelia.wilson@example.com", "mason.stewart@example.com", "emma.edwards@example.com",
            "liam.walker@example.com", "ava.turner@example.com", "noah.thomas@example.com",
            "olivia.green@example.com", "logan.hughes@example.com", "sophia.robinson@example.com",
            "jack.harris@example.com", "emma.clark@example.com", "lucas.carter@example.com",
            "mia.cooper@example.com", "ethan.murphy@example.com", "ava.hughes@example.com",
            "oliver.bennett@example.com", "isabella.moore@example.com", "noah.bailey@example.com",
            "sophia.evans@example.com", "lucas.mitchell@example.com", "mia.martin@example.com",
            "mason.king@example.com", "olivia.morris@example.com", "liam.roberts@example.com",
            "sophia.johnson@example.com", "jacob.hall@example.com", "emma.lewis@example.com",
            "ava.phillips@example.com", "oliver.williams@example.com", "mia.cook@example.com",
            "jack.davis@example.com", "isabella.anderson@example.com", "noah.smith@example.com",
            "sophia.miller@example.com", "lucas.jones@example.com", "olivia.harris@example.com",
            "jacob.martin@example.com", "emma.moore@example.com", "mia.smith@example.com",
            "oliver.wilson@example.com", "isabella.robinson@example.com", "jackson.miller@example.com",
            "sophia.jackson@example.com", "jacob.brown@example.com", "ava.white@example.com",
            "oliver.jones@example.com", "mia.morris@example.com", "lucas.cooper@example.com",
            "sophia.evans@example.com", "noah.anderson@example.com", "emma.mitchell@example.com"
        ]
        for i in range(10):
            f_name = driver.find_element(By.ID, "id_first_name")
            l_name = driver.find_element(By.ID, "id_last_name")
            email = driver.find_element(By.ID, "id_email")
            password = driver.find_element(By.ID, "id_password1")
            conf_pass = driver.find_element(By.ID, "id_password2")
            register_button = driver.find_elements(By.CLASS_NAME, "waves-light")[-1]

            random_name = names_list[fake.random_int(0, len(names_list))]
            first_name, last_name = random_name.split(" ")
            random_email = positive_emails[fake.random_int(0, len(positive_emails))]

            f_name.send_keys(first_name)
            l_name.send_keys(last_name)
            fake_password = fake.password()
            password.send_keys(fake_password)
            conf_pass.send_keys(fake_password)
            email.send_keys(random_email)
            register_button.click()
            time.sleep(1)
            driver.find_elements(By.CLASS_NAME, "waves-light")[-2].click()
            time.sleep(2)

        time.sleep(2)
    def test_neg_reg(self):
        driver = self.driver
        driver.get("http://99.153.249.66/")
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, "btn-outline-warning")[1].click()

        time.sleep(1)

        names_list = [
            "Eloise O'Reilly", "Leandre D'Amico", "Chloe D'Angelo", "Zoe O'Connell", "Celeste O'Malley",
            "Leo O'Leary", "Theodore D'Souza", "Anais O'Mara", "Ismael D'Costa", "Maelys O'Sullivan",
            "Noemie O'Malley", "Celine D'Arcy", "Nehemie O'Neal", "Cedric O'Dwyer", "Oceane D'Lorenzo",
            "Leonard D'Amore", "Zoe O'Brian", "Celia D'Agostino", "Matheo O'Callaghan", "Maelle O'Grady",
            "Theophile D'Angelo", "Lea O'Malley", "Raphael D'Costa", "Melodie O'Reilly", "Hugo D'Amico",
            "Lena O'Sullivan", "Nicolas O'Dwyer", "Leandro D'Souza", "Sarah O'Neal", "Baptiste O'Leary",
            "Ines D'Lorenzo", "Maxime D'Arcy", "Isabelle O'Mara", "Octave O'Connell", "Clara O'Brian",
            "Timeo O'Reilly", "Manon O'Leary", "Robin D'Amico", "Leo O'Neal", "Valentin O'Dwyer",
            "Margaux D'Costa", "Nathan O'Connell", "Oceane D'Souza", "Melina O'Malley", "Lucas O'Leary",
            "Roxane D'Arcy", "Gabriel O'Dwyer", "Emma D'Lorenzo", "Cedric O'Reilly", "Zoe O'Mara",
            "Leon D'Angelo", "Manon D'Amico", "Simon O'Sullivan", "Juliette D'Costa", "Ethan O'Connell",
            "Clemence O'Neal", "Maxence D'Souza", "Leane O'Reilly", "Antoine D'Amico", "Camille O'Dwyer",
            "Jules D'Lorenzo", "Raphael D'Souza", "Lena O'Malley", "Leo O'Reilly", "Margaux D'Arcy",
            "Theo O'Connell", "Emma O'Leary", "Alexandre D'Angelo", "Lena O'Mara", "Clement O'Dwyer",
            "Lucas D'Amico", "Manon D'Costa", "Hugo O'Connell", "Lou D'Souza", "Romain O'Neal",
            "Chloe D'Lorenzo", "Lea O'Dwyer", "Baptiste D'Angelo", "Oceane O'Reilly", "Raphael O'Connell",
            "Mathilde D'Amico", "Victor D'Souza", "Leonie D'Costa", "Noe O'Neal", "Maelle O'Leary",
            "Theo O'Dwyer", "Leon D'Lorenzo", "Juliette D'Angelo", "Jules O'Connell", "Lea O'Neal",
            "Maxime O'Dwyer", "Hugo D'Amore", "Lou D'Souza", "Manon D'Costa", "Leo O'Connell",
            "Celeste O'Neal", "Raphael D'Lorenzo", "Oceane D'Amico", "Lucas D'Arcy", "Chloe D'Souza" ]

        negative_emails = [
            "john.doe", "jane.smith@example", "alex.wilson@", "@example.com",
            "michael.brown@example.c", "sarah.johnson@example..com", "david.jackson@.com",
            "olivia.miller@example", "james.davis@", "emma.anderson", "william.thomas",
            "charles.robinson", "sophia.clark", "joseph.harris@", "mia.lewis",
            "george.lee@", "abigail.hall", "@example.com", "samuel.green@example",
            "isabella.turner@", "ethan.carter", "oliver.phillips", "ava.roberts",
            "amelia.baker@", "benjamin.walker", "emily.cook", "jacob.campbell",
            "chloe.kelly@", "mason.morgan", "sophia.james", "daniel.hughes",
            "mia.price@", "william.evans", "olivia.richardson", "alexander.cooper",
            "ava.bell@", "michael.collins", "amelia.cook", "david.murphy",
            "emma.bailey@", "james.stewart", "isabella.brown", "jackson.jenkins",
            "sophia.wood@", "oliver.parker", "mia.ward", "ethan.martin",
            "lily.harris@", "noah.mitchell", "ava.morris", "william.roberts",
            "olivia.campbell@", "daniel.phillips", "sophia.king", "logan.anderson",
            "isabella.hall@", "jackson.adams", "amelia.wilson", "mason.stewart",
            "emma.edwards@", "liam.walker", "ava.turner", "noah.thomas",
            "olivia.green@", "logan.hughes", "sophia.robinson", "jack.harris",
            "emma.clark@", "lucas.carter", "mia.cooper", "ethan.murphy",
            "ava.hughes@", "oliver.bennett", "isabella.moore", "noah.bailey",
            "sophia.evans@", "lucas.mitchell", "mia.martin", "mason.king",
            "olivia.morris@", "liam.roberts", "sophia.johnson", "jacob.hall",
            "emma.lewis@", "ava.phillips", "oliver.williams", "mia.cook",
            "jack.davis@", "isabella.anderson", "noah.smith", "sophia.miller",
            "lucas.jones@", "olivia.harris", "jacob.martin", "emma.moore",
            "mia.smith@", "oliver.wilson", "isabella.robinson", "jackson.miller",
            "sophia.jackson@", "jacob.brown", "ava.white", "oliver.jones",
            "mia.morris@", "lucas.cooper", "sophia.evans", "noah.anderson",
            "emma.mitchell@"]



        for i in range(10):
            f_name = driver.find_element(By.ID, "id_first_name")
            l_name = driver.find_element(By.ID, "id_last_name")
            email = driver.find_element(By.ID, "id_email")
            password = driver.find_element(By.ID, "id_password1")
            conf_pass = driver.find_element(By.ID, "id_password2")
            register_button = driver.find_elements(By.CLASS_NAME, "waves-light")[-1]

            random_name = names_list[fake.random_int(0, len(names_list))]
            first_name, last_name = random_name.split(" ")
            random_email = negative_emails[fake.random_int(0, len(negative_emails))]

            f_name.send_keys(first_name)
            l_name.send_keys(last_name)
            fake_password = fake.password()
            password.send_keys(fake_password)
            conf_pass.send_keys(fake_password)
            email.send_keys(random_email)
            register_button.click()
            time.sleep(1)
            invalid_email = driver.find_element(By.CLASS_NAME, "invalid-feedback").text


            if invalid_email == "Enter a valid email address.":
                print("Negative test Pass with incorecct email:" ,random_email )
            else:
                print("Negative Email is Fail with invalid email:", random_email)


    def tearDown(self):
        self.driver.quit()
