import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class FindElementById:
    def locateByID(self):
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver.get("https://vk.com/")
        driver.find_element(value='index_email').send_keys("SomeTestData")
        time.sleep(10)

vklogin = FindElementById()
vklogin.locateByID()
