from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
#just copy code from lesson 39, but use implicity wait
class yoink42:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        mouse = ActionChains(driver)
        driver.get("https://jqueryui.com/droppable/")
        driver.implicitly_wait(5)
        driver.switch_to.frame(driver.find_element(By.XPATH,"(//iframe[@class='demo-frame'])[1]"))
        driver.maximize_window()
        mouse.drag_and_drop_by_offset(driver.find_element(By.XPATH,"//div[@id='draggable']"), 150, 20).perform()



a = yoink42()
a.yoink()
