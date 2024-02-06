import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowOpens = driver.window_handles

driver.switch_to.window(windowOpens[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(windowOpens[0])
print(driver.find_element(By.TAG_NAME, "h3").text)