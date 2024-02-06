from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#FireFox
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# class name, id, name linkText, cssselector, xpath
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath // tagname[@attribute='value'] -> //input[@type='submit']
# CSSSecletor // tagname[@attribute='value'] -> //input[@type='submit'], #id .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ajay")
#driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("bijay")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "successfully!" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hellow")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
