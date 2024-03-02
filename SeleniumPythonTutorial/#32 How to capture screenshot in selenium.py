from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class makeScreen:
    def yoink(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://vk.com/")
        time.sleep(2)
        button = driver.find_element(By.XPATH,"//button[@type='submit']//span[@class='FlatButton__in']")
        button.screenshot(".\\lesson32screen.png")
        button.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Users\\Альфи\\PycharmProjects\\PythonAutomationLearning\\SeleniumPythonTutorial\\lesson32secondscreen.png")
        driver.save_screenshot(".\\lesson32thirdscreen.png")
a = makeScreen()
a.yoink()