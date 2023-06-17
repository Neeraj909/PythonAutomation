import time

from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("--ignore-certification-errors")
service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj,options=chrome_option)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)