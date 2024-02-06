import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--ingnore-certificates-errors")
service_obj = Service("C:\\Users\\anaru\\OneDrive\\Desktop\\personal\\chromedriver.exe")
driver = webdriver.Firefox(service=service_obj, options=chrome_option)
driver.implicitly_wait(5)
#5 second is max time out
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")