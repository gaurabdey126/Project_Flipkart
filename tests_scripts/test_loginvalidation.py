import time
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from utilities.baseClass import BaseClass
from pages.login_page import LoginPage
from test_data.LoginPageData import LoginPageData


class Test_LoginValidation(BaseClass):
    #TC 1
    @allure.severity(severity_level="MEDIUM")
    def test_Login_no_number(self):
        loginpage =LoginPage(self.driver)
        loginpage.getcross_mark().click()
        loginpage.getlogin_btn().click()
        loginpage.getrequest_otp().click()

        err_msg = loginpage.getotp_error().text
        assert "ID/Mobile number" in err_msg
        print(err_msg)

    #TC 2
    @allure.severity(severity_level="HIGH")
    def test_login_password(self, getData):
        loginpage = LoginPage(self.driver)
        loginpage.getcross_mark().click()
        loginpage.getlogin_btn().click()
        loginpage.getenter_mobile().send_keys(getData["Mobile"])
        loginpage.getenter_pwd().send_keys(getData["Pwd"])
        loginpage.getsubmit_btn().click()

        ## LOGOUT Functionality
        self.get_hover(loginpage.getmy_account())
        loginpage.getlogout().click()
        assert "Login" in (loginpage.getlogin_btn().text)
        print("Logged out SUCCESSFULLY")

    # #TC 3
    # def test_login_number_otp(self, getData):
    #     loginpage = LoginPage(self.driver)
    #     loginpage.getcross_mark().click()
    #     loginpage.getlogin_btn().click()
    #     loginpage.getenter_mobile().send_keys(getData["Mobile"])
    #     loginpage.getrequest_otp().click()
    #
    #     self.get_explicitwait(loginpage.getotp_value())
    #
    #     loginpage.getverify_btn().click()
    #     print("Login is success")
    #
    #     ## LOGOUT Functionality
    #     self.get_hover(loginpage.getmy_account())
    #     loginpage.getlogout().click()
    #     assert "Login" in (loginpage.getlogin_btn().text)
    #     print("Logged out SUCCESSFULLY")



    @pytest.fixture(params=LoginPageData.loginpage_data)
    def getData(self,request):
        return request.param


