from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class OhMyClass:
    def checkBox(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.maximize_window()
        check = driver.find_element(By.XPATH, "//input[@value='red']").click()
        check = driver.find_element(By.XPATH,"//input[@value='red']").is_selected()
        if check:
            print("Checkbox selected")
        else:
            print("Checkbox is not selected")

example = OhMyClass()
example.checkBox()