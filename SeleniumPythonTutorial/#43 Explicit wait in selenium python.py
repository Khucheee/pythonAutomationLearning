from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
class yoink:
    def yo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 10)
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



one = yoink()
one.yo()