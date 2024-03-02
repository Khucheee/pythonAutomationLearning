from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
class yoink39:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        mouse = ActionChains(driver)
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.XPATH,"(//iframe[@class='demo-frame'])[1]"))
        driver.maximize_window()
        time.sleep(5)
        mouse.drag_and_drop_by_offset(driver.find_element(By.XPATH,"//div[@id='draggable']"), 150, 20).perform()
        time.sleep(5)



a = yoink39()
a.yoink()
