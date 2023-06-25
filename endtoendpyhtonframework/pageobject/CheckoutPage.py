from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    promoCode = (By.CSS_SELECTOR, ".promoCode")
    promoBtn = (By.CSS_SELECTOR, ".promoBtn")
    promoInfo = (By.CSS_SELECTOR, ".promoInfo")

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def enterPromoCode(self):
        return self.driver.find_element(*CheckoutPage.promoCode)

    def promoButton(self):
        return self.driver.find_element(*CheckoutPage.promoBtn)

    def promoInfoText(self):
        return self.driver.find_element(*CheckoutPage.promoInfo)
