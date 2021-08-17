from selenium.webdriver.common.by import By


class ProductDetailsPage:
    def __init__(self,driver):
        self.driver = driver

    add_to_cart = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")



    def getadd_to_cart(self):
        return self.driver.find_element(*ProductDetailsPage.add_to_cart)