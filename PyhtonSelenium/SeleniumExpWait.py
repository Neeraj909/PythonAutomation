import time

from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

products = driver.find_elements(By.CSS_SELECTOR,".products .product-action")
for product in products:
    product.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
assert "Code applied ..!" in driver.find_element(By.CSS_SELECTOR,".promoInfo").text
amounts=driver.find_elements(By.XPATH,"//tbody//td[5]//p[@class='amount']")
totalAmountSum = 0
for amount in amounts:
    totalAmountSum = totalAmountSum+int(amount.text)
print(totalAmountSum)
totalAmount = driver.find_element(By.CLASS_NAME,"totAmt").text
print(totalAmount)
assert totalAmountSum == int(totalAmount)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

