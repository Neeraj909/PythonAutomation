from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR, ".search-keyword")
    products = (By.CSS_SELECTOR, ".products .product-action")
    cart = (By.CSS_SELECTOR, "img[alt='Cart']")

    def searchText(self):
        return self.driver.find_element(*HomePage.search)

    def selectProduct(self):
        return self.driver.find_elements(*HomePage.products)

    def cartButton(self):
        return self.driver.find_element(*HomePage.cart)
