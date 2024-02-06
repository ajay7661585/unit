from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver
#service_obj = Service() # selenium manager
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://google.com")

#Chrome
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#FireFox
#service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\geckodriver.exe")
#driver = webdriver.Firefox(service=service_obj)

#Microsoft
#service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\msedgedriver.exe")
#driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
