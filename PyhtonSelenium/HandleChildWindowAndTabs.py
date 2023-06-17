import time

from selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(2)
driver.find_element(By.ID,"openwindow").click()
time.sleep(4)
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
driver.close()
driver.switch_to.window(windows[0])
print(driver.title)


