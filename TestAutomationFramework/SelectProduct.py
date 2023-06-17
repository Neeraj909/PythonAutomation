import time

from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(4)
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH,"//div//h4//a").text
    if productName in "iphone X":
        product.find_element(By.XPATH,"//div[@class='card-footer']//button").click()
        break
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("India")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class='suggestions']")))
driver.find_element(By.CSS_SELECTOR,"div[class='suggestions']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[class='btn btn-success btn-lg']").click()
assert "Thank you! Your order will be delivered in next few weeks" in driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
time.sleep(5)
