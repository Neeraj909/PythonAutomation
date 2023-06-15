from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver
service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Neeraj")
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("Hello@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()
#static dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
message=driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
assert "Success" in message
driver.close()
