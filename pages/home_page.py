from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search_field = (By.XPATH, "//input[@type='text']")
    def getsearchfield(self):
        return self.driver.find_element(*HomePage.search_field)