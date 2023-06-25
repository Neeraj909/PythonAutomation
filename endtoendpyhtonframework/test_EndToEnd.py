import time

from selenium.webdriver.common.by import By

from endtoendpyhtonframework.pageobject.CheckoutPage import CheckoutPage
from endtoendpyhtonframework.pageobject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_end_to_end(self):
        print(self.driver.title)
        print(self.driver.current_url)
        homePage = HomePage(self.driver)
        homePage.searchText().send_keys("Br")
        time.sleep(4)
        products = homePage.selectProduct()
        for product in products:
            product.click()
        homePage.cartButton().click()
        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.checkoutButton().click()
        checkoutPage.enterPromoCode().send_keys("rahulshettyacademy")
        checkoutPage.promoButton().click()
        self.waitForElement(".promoInfo")
        print(checkoutPage.promoInfoText().text)
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
