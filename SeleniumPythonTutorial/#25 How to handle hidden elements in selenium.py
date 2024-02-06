from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class A:
    def a(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://translate.google.com/")
        d.maximize_window()
        t = d.find_element(By.XPATH, "//a[contains(text(),'Правила и принципы')]").is_displayed()
        print(t)
        time.sleep(5)
        d.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M3 18h18v-')]").click()
        time.sleep(5)
        t = d.find_element(By.XPATH,"//a[contains(text(),'Правила и принципы')]").is_displayed()
        print(t)

pop = A()
pop.a()