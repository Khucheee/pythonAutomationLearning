import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#did not use tag name becouse too much elements with tag
class newOne:
    def css(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com")
        a = d.find_elements(by="tag name",value='input')
        print(len(a))
        for i in a:
            print(i. __class__)
a = newOne()
a.css()