from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class yoink:
    def yo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://yatra.com/")
        depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        suggestions = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(suggestions))



one = yoink()
one.yo()