import json
import hashlib
import time
from random import uniform, randint
from collections import Counter
import aiohttp
import asyncio
from aiohttp.client_exceptions import ClientConnectorError
import requests
from selenium import webdriver, common
from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, ElementNotInteractableException, InvalidArgumentException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as OperaService
from urllib3.util import wait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from seleniumwire import webdriver as SWWD


class Project_s:

    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://testpages.herokuapp.com/")


    def home(self):
        self.driver.get("https://testpages.herokuapp.com/")
        assert_title(driver, "Selenium Test Pages")
        # wait.until(EC.element_to_be_clickable((By.XPATH


    def assert_title(driver, title):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is(title))
        assert title in driver.title
        print("Page has", driver.title + " as Page title")
    # Screenshot of the page
        driver.get_screenshot_as_file(f"Page {title}.png")
        if not title in driver.title:
            raise Exception(f"Page {title} has wrong Title!")



     home()


