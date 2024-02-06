from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
name = "Ajay"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
assert name in alerttext
print(alerttext)
alert.accept()