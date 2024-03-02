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
        dd = driver.find_element(By.XPATH,"//select[@name='select']")
        dropDown = Select(dd)
        dropDown.select_by_index(0)
        time.sleep(2)
        dropDown.select_by_visible_text("Крокодил Гена")
        time.sleep(2)
        dropDown.select_by_visible_text("Шапокляк")
        time.sleep(2)
        dropDown.deselect_all()
        time.sleep(2)
        #dropDown.select_by_value() there was no value in the option tag :(

a = MyClass()
a.functi()