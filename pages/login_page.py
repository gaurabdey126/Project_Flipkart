from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    cross_mark = (By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
    login_btn = (By.XPATH, "//a[text()='Login']")
    enter_mobile = (By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    enter_pwd = (By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']")
    submit_btn = (By.XPATH, "//button[@type='submit'][@class='_2KpZ6l _2HKlqd _3AWRsL']")
    request_otp = (By.XPATH, "//button[text()='Request OTP']")
    otp_error = (By.XPATH, "//span[contains(text(),'Please')]")
    otp_value = (By.CSS_SELECTOR, ".HSKgdN")
    verify_btn = (By.XPATH, "//button[text()='Verify']")
    logout = (By.XPATH, "//div[text()='Logout']")
    my_account = (By.XPATH, "//div[text()='My Account']")




    def getcross_mark(self):
        return self.driver.find_element(*LoginPage.cross_mark)

    def getlogin_btn(self):
        return self.driver.find_element(*LoginPage.login_btn)

    def getenter_mobile(self):
        return self.driver.find_element(*LoginPage.enter_mobile)

    def getenter_pwd(self):
        return self.driver.find_element(*LoginPage.enter_pwd)

    def getsubmit_btn(self):
        return self.driver.find_element(*LoginPage.submit_btn)

    def getrequest_otp(self):
        return self.driver.find_element(*LoginPage.request_otp)

    def getotp_error(self):
        return self.driver.find_element(*LoginPage.otp_error)

    def getotp_value(self):
        return self.driver.find_element(*LoginPage.otp_value)

    def getverify_btn(self):
        return self.driver.find_element(*LoginPage.verify_btn)

    def getmy_account(self):
        return self.driver.find_element(*LoginPage.my_account)

    def getlogout(self):
        return self.driver.find_element(*LoginPage.logout)