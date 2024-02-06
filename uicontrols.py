from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radio = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
print(len(radio))

for radioButton in radio:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        assert radioButton.is_selected()
        break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
