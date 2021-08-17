from selenium.webdriver.common.by import By


class CartVerifyPage:
    def __init__(self, driver):
        self.driver = driver

    inrease_item = (By.XPATH, "//button[text()='+']")
    decrease_item = (By.XPATH, "//button[text()='–']")
    place_order = (By.XPATH, "//span[text()='Place Order']")
    remove = (By.XPATH, "//div[text()='Remove']")
    total_amount = (By.XPATH, "//div[@class='Ob17DV _3X7Jj1']/span")
    alert_remove = (By.XPATH, "//div[@class='_3dsJAO _24d-qY FhkMJZ']")
    alert_cancel = (By.XPATH, "//div[@class='_3dsJAO _24d-qY RxvIII']")

    def getinrease_item(self):
        return self.driver.find_element(*CartVerifyPage.inrease_item)
    def getdecrease_item(self):
        return self.driver.find_element(*CartVerifyPage.decrease_item)
    def getplace_order(self):
        return self.driver.find_element(*CartVerifyPage.place_order)
    def getremove(self):
        return self.driver.find_element(*CartVerifyPage.remove)
    def gettotal_amount(self):
        return self.driver.find_element(*CartVerifyPage.total_amount)
    def getalert_cancel(self):
        return self.driver.find_element(*CartVerifyPage.alert_cancel)
    def getalert_remove(self):
        return self.driver.find_element(*CartVerifyPage.alert_remove)
