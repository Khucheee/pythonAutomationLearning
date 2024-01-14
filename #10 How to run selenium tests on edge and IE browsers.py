from selenium import webdriver
driver = webdriver.Edge()
driver.get("http://vk.com")
driver.maximize_window()
print(driver.title)
driver.close()
