from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class A:
    def a(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://vk.com/")
        t = d.find_element(By.XPATH,"//div[@id='index_login']//span[@class='FlatButton__in']//span[1]").get_attribute("class")
        print(t)

pop = A()
pop.a()