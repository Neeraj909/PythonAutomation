import time

from selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver
service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#handle checkbox dynamically
checkboxes=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()

        break
#handle radio button
radiobuttons=driver.find_elements(By.CSS_SELECTOR,"input[name='radioButton']")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()

        break
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()

#handle alert button
driver.find_element(By.CSS_SELECTOR,"input[name='enter-name']").send_keys("Neeraj")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)
alert = driver.switch_to.alert
assert "Neeraj" in alert.text
alert.accept()

## mouse over
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
time.sleep(4)





