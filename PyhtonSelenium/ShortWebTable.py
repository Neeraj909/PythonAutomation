import time

from selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
webShortVeg=[]
service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,"//a[@class='cart-header-navlink' and text()='Top Deals']").click()
window = driver.window_handles
driver.switch_to.window(window[1])
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
vegTables = driver.find_elements(By.XPATH,"//tr//td[1]")
for vegTable in vegTables:
    webShortVeg.append(vegTable.text)

shortVeg = webShortVeg.copy()

webShortVeg.sort()
print(webShortVeg)
print(shortVeg)
assert webShortVeg == shortVeg
time.sleep(5)