import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#я не нашел сайта с примером параметра a ref, на который завязывается Link text
class newOne:
    def css(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com")
        d.find_element(by='link text',value='Телефон или почта').send_keys("Login has been found by link text")
        d.find_element(by='partial link text', value = 'Войт').click()
        time.sleep(3)
a = newOne()
a.css()