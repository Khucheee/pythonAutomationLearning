from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class makeScreen:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver.get("https://vk.com/")
        driver.execute_script('window.open("https://vk.com/", "_self");')
        time.sleep(3)
        button = driver.execute_script("return document.getElementsByClassName('FlatButton__in')[3];")
        time.sleep(2)
        driver.execute_script("arguments[0].click()",button)
        time.sleep(2)
a = makeScreen()
a.yoink()