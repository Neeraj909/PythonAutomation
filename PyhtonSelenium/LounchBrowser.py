from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
#chrome driver
service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)

# service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/geckodriver")
# driver = webdriver.Firefox(service = service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.close()


