import time

from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

products = driver.find_elements(By.CSS_SELECTOR,".products .product-action")
for product in products:
    product.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
driver.find_element(By.CSS_SELECTOR,".promoInfo").is_displayed()
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
assert "Code applied ..!" in driver.find_element(By.CSS_SELECTOR,".promoInfo").text

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

