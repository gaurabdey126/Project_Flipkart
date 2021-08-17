import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    #HOVER Method
    def get_hover(self,locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()


    def get_alert_yes(self,driver):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def get_alert_no(self,driver):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    #EXPLICIT WAIT
    def get_explicitwait(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))