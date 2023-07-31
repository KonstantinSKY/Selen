import tarfile
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
from selenium.webdriver.common.alert import Alert

faker_indent = Faker()


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
        driver.find_element(By.ID, "htmlformtest").click()  # next page HTML Form Example
        check_box_random = randint(0, 2)
        driver.find_elements(By.NAME, "radioval")[randint(0, 2)].click()  # click random radio every time

        driver.find_elements(By.NAME, "checkboxes[]")[check_box_random].click()  # click random checkbox every time
        time.sleep(5)

        Select(driver.find_element(By.NAME, 'dropdown')).select_by_index(
            randint(0, 5))  # choosing random dropdown by Select
        Select(driver.find_element(By.NAME, "multipleselect[]")).select_by_index(
            randint(0, 3))  # Multiple Select Values

        driver.find_elements(By.NAME, "submitbutton")[1].click()
        time.sleep(5)
        # checking if random checkbox have same value with submited form
        submit_form = driver.find_element(By.ID, "_valuecheckboxes0").text

        if "cb" + str(check_box_random + 1) == submit_form:
            print("Form OK")
        else:
            print("Form Bad")

        time.sleep(10)

    def test_Dynamic_HTML_TABLE_Tag(self):
        driver = self.driver

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
        text_website = driver.find_element(By.XPATH, "//h1[contains(.,'Dynamic HTML TABLE Tag')]").text
        text_expected = "Dynamic HTML TABLE Tag"
        if text_website == text_expected:
            try:
                assert text_website == text_expected
                print("Paragraph text is correct. Current text is:", text_website)
            except AssertionError:
                print("Paragraph text is different. Current text is:", text_website)
        driver.find_element(By.TAG_NAME, "p")  # checking first paragraph
        driver.find_element(By.ID, "refreshtable")  # refresh table button
        driver.find_element(By.ID, "caption")  # placeholder Caption
        driver.find_element(By.ID, "tableid")  # placeholder Id

        elems = driver.find_elements(By.TAG_NAME, "a")
        print(type(elems))
        print(elems)

        for elem in elems:

            xpath = driver.execute_script("""
                    var xpath = "";
                    var containerElem = document.documentElement;
                    var elem = arguments[0];

                    while (elem !== containerElem) {
                        var index = 0;
                        var sibling = elem.previousSibling;

                        while (sibling) {
                            if (sibling.nodeType === Node.ELEMENT_NODE && 
                                sibling.nodeName.toLowerCase() === elem.nodeName.toLowerCase()) {
                                index++;
                            }
                            sibling = sibling.previousSibling;
                        }
                        xpath = "/" + elem.nodeName.toLowerCase() + "[" + (index + 1) + "]" + xpath;
                        elem = elem.parentNode;
                    }
                    return "/" + containerElem.nodeName.toLowerCase() + xpath;
            """, elem)  # Checking for correct XPATH
            print("xpath", xpath)
            if elem.get_attribute("hrefd"):
                print("OK for Elements", elem.text)

            else:
                print("NOT OK  for Element", elem.text)

        driver.find_element(By.TAG_NAME, "summary").click()  # Table data
        jsondata = driver.find_element(By.ID, "jsondata")
        jsondata.clear()  # placeholder with json textarea

        data = [{"name" : "Bob", "age" : 20}, {"name": "George", "age" : 42}, {"name" : "Max", "age" : 20}]


        print(data)

        for i in range(100):
            data.append({"name":faker_indent.first_name(), "age": randint(10, 100)})
            print(data)

        time.sleep(1)

        print(data)
        jsondata.send_keys(str(data).replace("'", '"'))
        time.sleep(4)

        driver.find_element(By.ID, "refreshtable").click()
        time.sleep(10)
        Allelems = driver.find_elements(By.TAG_NAME, "tr")

        if len(Allelems[1:]) == len(data):
            print("lenght is ok")
        else:
            print("lenght is not ok")

        i = 0
        for elem in Allelems[1:]:

            tds = elem.find_elements(By.TAG_NAME,"td")
            if tds[0].text == data[i]["name"] and tds[1].text == str(data[i]["age"]):
                print("OK")
            else:
                print("Not OK", tds[0], "is", data[i]["name"], tds[1],"is", data[i]["age"] )
            i += 1




    def test_Alert_Box_Examples(self):
        driver = self.driver
        driver.get("https://testpages.herokuapp.com/")
        driver.find_element(By.ID, "alerttest").click()
        text_website = driver.find_element(By.TAG_NAME, "h1").text
        text_expected = "Alert Box Examples"
        try:
            assert text_website == text_expected
            print("Paragraph text is correct. Current text is:", text_website)
        except AssertionError:
            print("Paragraph text is different. Current text is:", text_website)

        button1 = driver.find_element(By.ID, "alertexamples")  # Button - Show alert box
        button1.click()
        alert = Alert(driver)
        print(alert.text)
        time.sleep(4)
        alert.accept()
        time.sleep(3)
        button2 = driver.find_element(By.ID, "confirmexample")  # Button - Show confirm box
        button3 = driver.find_element(By.ID, "promptexample")  # Button - Show prompt box
        paragraph_website = driver.find_element(By.TAG_NAME, "p").text
        paragraph_expected = "There are three main JavaScript methods which show alert dialogs: alert," \
                             " confirm and prompt. This page has examples of each."

        try:
            assert paragraph_website == paragraph_expected
            print("Paragraph text is correct. Current text is:", paragraph_website)
        except AssertionError:
            print("Paragraph text is different. Current text is:", paragraph_website)

        button2.click()
        alert = Alert(driver)
        print(alert.text)
        time.sleep(4)
        alert.accept()
        if driver.find_element(By.ID, "confirmreturn").text == "true":
            print("OK")
        else:
            print("Not OK")

        time.sleep(3)
        button2.click()
        time.sleep(3)
        alert.dismiss()
        time.sleep(3)

        button3.click()
        time.sleep(3)
        alert.send_keys("Max")
        time.sleep(3)
        alert.accept()
        time.sleep(3)
        if driver.find_element(By.ID, "promptreturn").text == "Max":
            print("OK")
        else:
            print("Not OK")

    def test_Refresh_Page_Test(self):
        driver = self.driver
        driver.get("https://testpages.herokuapp.com/styled/refresh")
        value1 = driver.find_element(By.ID, "embeddedrefreshdatevalue").text
        value2 = driver.find_element(By.ID, "refreshdate").text
        value3 = driver.find_element(By.TAG_NAME, "h1").text.split()[-1]
        driver.refresh()
        time.sleep(5)
        if value3 == value2 == value1:
            print("after Page Refresh the id numbers equal")
        else:
            print("ERROR after Page Refresh the id numbers  is not equal", value3, value1, value2)
        driver.find_element(By.LINK_TEXT, "EvilTester.com").click()
        time.sleep(3)
        driver.close()











    def tearDown(self):
        self.driver.quit()
