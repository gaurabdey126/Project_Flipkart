from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    cross_mark = (By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
    def getcrossmark(self):
        return self.driver.find_element(*LoginPage.cross_mark)

    login_button = (By.XPATH, "//a[text()='Login']")
    def getloginbutton(self):
        return self.driver.find_element(*LoginPage.login_button)

    enter_mobile = (By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    def getmobile(self):
        return self.driver.find_element(*LoginPage.enter_mobile)

    enter_pwd = (By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']")
    def getpassword(self):
        return self.driver.find_element(*LoginPage.enter_pwd)

    submit_button = (By.XPATH, "//button[@type='submit'][@class='_2KpZ6l _2HKlqd _3AWRsL']")
    def getsubmit(self):
        return self.driver.find_element(*LoginPage.submit_button)

    request_otp = (By.XPATH, "//button[text()='Request OTP']")
    def getrequestotp(self):
        return self.driver.find_element(*LoginPage.request_otp)

    otp_error = (By.XPATH, "//span[contains(text(),'Please')]")
    def getotperror(self):
        return self.driver.find_element(*LoginPage.otp_error)

    otp_value = (By.CSS_SELECTOR, ".HSKgdN")
    def getotpvalue(self):
        return self.driver.find_element(*LoginPage.otp_value)

    verify_button = (By.XPATH, "//button[text()='Verify']")
    def getverifybutton(self):
        return self.driver.find_element(*LoginPage.verify_button)
