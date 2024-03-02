from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class yoink34:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        firstWindow = driver.current_window_handle
        driver.find_element(By.XPATH,"//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        windows = driver.window_handles
        for window in windows:
            if window!=firstWindow:
                driver.switch_to.window(window)
                time.sleep(5)
                driver.find_element(By.XPATH, "//a[normalize-space()='customer care']")
                time.sleep(2)
                driver.close()
                break
        driver.switch_to.window(firstWindow)
        driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()



a = yoink34()
a.yoink()