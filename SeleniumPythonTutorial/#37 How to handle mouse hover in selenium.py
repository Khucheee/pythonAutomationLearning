from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
class yoink36:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        mouse = ActionChains(driver)
        driver.get("https://finuslugi.ru/")
        driver.maximize_window()
        mouse.move_to_element(driver.find_element(By.XPATH,"(//div[@class='main-menu__link-content'])[1]")).perform()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Все вклады").click()
        time.sleep(5)





a = yoink36()
a.yoink()