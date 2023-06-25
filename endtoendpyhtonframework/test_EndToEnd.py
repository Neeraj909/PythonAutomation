from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_end_to_end(self):
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

        products = self.driver.find_elements(By.CSS_SELECTOR, ".products .product-action")
        for product in products:
            product.click()

        self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
        self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

        self.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
        self.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
        print(self.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
        assert "Code applied ..!" in self.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
        amounts = self.driver.find_elements(By.XPATH, "//tbody//td[5]//p[@class='amount']")
        totalAmountSum = 0
        for amount in amounts:
            totalAmountSum = totalAmountSum + int(amount.text)
        print(totalAmountSum)
        totalAmount = self.driver.find_element(By.CLASS_NAME, "totAmt").text
        print(totalAmount)
        assert totalAmountSum == int(totalAmount)
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        print("Completed")
