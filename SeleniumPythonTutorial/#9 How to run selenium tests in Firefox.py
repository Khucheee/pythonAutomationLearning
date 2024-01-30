from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://vk.com")
driver.maximize_window()
print(driver.title)
driver.close()
