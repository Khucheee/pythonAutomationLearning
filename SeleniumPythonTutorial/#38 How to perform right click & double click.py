from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
class yoink38:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        mouse = ActionChains(driver)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        mouse.context_click(driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")).perform()
        mouse.double_click(driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")).perform()
        driver.switch_to.alert.accept()

a = yoink38()
a.yoink()
