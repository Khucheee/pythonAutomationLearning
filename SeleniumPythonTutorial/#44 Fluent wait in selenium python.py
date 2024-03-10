from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
# difference is in 2 additional arguments
# 1 - how frequently we want to check value
# 2 - what exceptions we want to be ignored
class yoink44:
    def yo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 10,2,ignored_exceptions=[ElementClickInterceptedException]) # here is the difference
        driver.get("https://yatra.com/")
        driver.maximize_window()
        depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//div)[69]"))).find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']").send_keys("new")
        suggestions = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div)[69]"))).find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        for i in suggestions:
            print(i.text, "это предложение")



one = yoink44()
one.yo()