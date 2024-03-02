from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

class MyClass:
    def functi(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://htmlbook.ru/html/select")
        dd = driver.find_element(By.XPATH,"//select[@name='select2']")
        dropDown = Select(dd)
        dropDown.select_by_index(1)
        time.sleep(5)
        dropDown.select_by_visible_text("Крокодил Гена")
        time.sleep(3)
        #dropDown.select_by_value() there was no value in the option tag :(

a = MyClass()
a.functi()