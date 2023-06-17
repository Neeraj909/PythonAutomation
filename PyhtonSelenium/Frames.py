import time

from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
#chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certification-errors")

service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
# for headless browser
#driver = webdriver.Chrome(service=service_obj,options=chrome_option)
driver = webdriver.Chrome(service=service_obj,options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(2)
driver.switch_to.frame("courses-iframe")
print(driver.find_element(By.CSS_SELECTOR,".top-left ul li ").text)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").text)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.get_screenshot_as_file("screen.png")
