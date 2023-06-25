import pytest
from selenium  import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def driverSetup(request):
    service_obj = Service("/Users/neeraj.b.sharma/Downloads/pythonBasics/chromedriver")
    driver = webdriver.Chrome(service = service_obj)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
