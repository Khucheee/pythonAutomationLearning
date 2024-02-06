from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class A:
    def a(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        d.get("https://private.auth.alfabank.ru/passport/cerberus-mini-blue/dashboard-blue/username?response_type=code&client_id=newclick-web&scope=openid%20newclick-web&acr_values=username&non_authorized_user=true")
        t = d.find_element(By.XPATH,"//button[@type='submit']").is_enabled()
        if not t:
            print("test 1 pass")
        else:
            print("test 2 failed")
        d.find_element(By.XPATH,"//input[@aria-label='Логин']").send_keys("aaaaaa")
        d.find_element(By.XPATH, "//input[@aria-label='Пароль']").send_keys("aaaaaa")
        t = d.find_element(By.XPATH, "//button[@type='submit']").is_enabled()
        if t:
            print("test 2 pass")
        else:
            print("test 2 failed")

        time.sleep(2)
        print(t)

pop = A()
pop.a()