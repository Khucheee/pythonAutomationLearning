from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class yoink36:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert2")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        driver.switch_to.alert.accept()
        driver.switch_to.default_content()
        driver.find_element(By.XPATH,"//a[@id='menuButton']")





a = yoink36()
a.yoink()