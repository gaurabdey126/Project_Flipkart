from selenium.webdriver.common.by import By


class ProductListPage:
    def __init__(self, driver):
        self.driver = driver

    # // div[@class ='_2kHMtA']
    prod_name = (By.XPATH, "// div[@ class ='_4rR01T']")
    prod_details = (By.XPATH, "// li[@ class ='rgWa7D'][1]")




    def getprod_name(self):
        return self.driver.find_elements(*ProductListPage.prod_name)

    def getprod_details(self):
        return self.driver.find_elements(*ProductListPage.prod_details)
