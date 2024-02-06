import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
veggieSorted = []
#5 second is max time out
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")

for veggielement in veggieWebElement:
    veggieSorted.append(veggielement.text)
originalSorted = veggieSorted.copy()
print(originalSorted)
veggieSorted.sort()
print(veggieSorted)

assert originalSorted == veggieSorted