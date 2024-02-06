import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
class newOne:
    def css(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com")
        d.find_element(by='css selector',value='#index_email').send_keys("Login has been found by css")
        time.sleep(5)
a = newOne()
a.css()