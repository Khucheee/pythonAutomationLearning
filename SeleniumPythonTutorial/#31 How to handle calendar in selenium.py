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
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        time.sleep(1)
        depart_from.click()
        time.sleep(1)
        depart_from.send_keys("New Delhi")
        time.sleep(1)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(1)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New York")
        going_to.send_keys(Keys.ENTER)
        calendar = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        calendar.click()
        time.sleep(2)
        dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        time.sleep(1)
        for date in dates:
            if date.get_attribute("data=date")=="30/03/2024":
                date.click()
                print("We found date, that we need to buy tickets boi!")
                break

one = yoink()
one.yo()