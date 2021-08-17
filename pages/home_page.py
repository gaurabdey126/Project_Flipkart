from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search_field = (By.XPATH, "//input[@type='text']")
    search_icon = (By.XPATH, "//button[@class='L0Z3Pu']")






    def getsearch_field(self):
        return self.driver.find_element(*HomePage.search_field)


    def getsearch_icon(self):
        return self.driver.find_element(*HomePage.search_icon)