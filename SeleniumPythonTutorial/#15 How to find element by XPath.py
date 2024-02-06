from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
class FindByXPath:
    def Login(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com/")
        d.find_element(by='xpath',value = "//input[@id='index_email']").send_keys("avrora")
        time.sleep(5)
a = FindByXPath()
a.Login()
