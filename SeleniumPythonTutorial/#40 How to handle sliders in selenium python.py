from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
class yoink40:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        mouse = ActionChains(driver)
        driver.maximize_window()
        driver.get("https://www.mvideo.ru/brand/apple-685?categoryId=10")
        left = driver.find_element(By.XPATH,"//div[@id='Price-section']//a[1]")
        right = driver.find_element(By.XPATH,"(//a[@class='ui-slider-handle ui-state-default ui-corner-all'])[2]")
        time.sleep(2)
        #сдвигаем левый слайдер на 60 пикселей
        mouse.drag_and_drop_by_offset(left, 60, 0).perform()
        #сдвигаем правый слайдер на 50 пикселей
        mouse.click_and_hold(right).pause(1).move_by_offset(-50,0).release().perform()
        time.sleep(2)

a = yoink40()
a.yoink()
