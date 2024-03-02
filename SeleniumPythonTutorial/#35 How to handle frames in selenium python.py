from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class yoink35:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='W3Schools HTML Tutorial']"))
        driver.find_element(By.XPATH,"//a[@title='CSS Tutorial'][normalize-space()='CSS']").click()




a = yoink35()
a.yoink()