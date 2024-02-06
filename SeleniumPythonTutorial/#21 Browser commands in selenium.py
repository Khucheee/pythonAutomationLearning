import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class newOne:
    def browse(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com")
        print(d.current_url)
        print(d.title)
        d.maximize_window()
        d.minimize_window()
        d.find_element(By.XPATH,"//div[@class='page_block']//span[@class='FlatButton__in']//span[1]").click()
        d.back()
        d.refresh()
        d.forward()
        d.back()
        d.find_element(by='class name',value='VkIdForm__input').send_keys("Login has been found by tag name")
        d.find_element(by='class name',value='FlatButton__content').click()
        time.sleep(5)
a = newOne()
a.browse()