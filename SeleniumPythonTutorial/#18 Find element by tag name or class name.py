import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#did not use tag name becouse too much elements with tag
class newOne:
    def css(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com")
        d.find_element(by='class name',value='VkIdForm__input').send_keys("Login has been found by tag name")
        d.find_element(by='class name',value='FlatButton__content').click()
        time.sleep(5)
a = newOne()
a.css()