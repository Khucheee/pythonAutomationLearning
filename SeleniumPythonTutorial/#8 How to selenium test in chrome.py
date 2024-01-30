from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://vk.com")
driver.maximize_window()
print(driver.title)
driver.close()
