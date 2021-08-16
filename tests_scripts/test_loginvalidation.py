import time

import pytest
from utilities.baseClass import BaseClass
from pages.login_page import LoginPage
from test_data.LoginPageData import LoginPageData


class Test_LoginValidation(BaseClass):
    #TC 1
    def test_LoginwithoutNumber(self):
        loginpage =LoginPage(self.driver)

        loginpage.getcrossmark().click()

        loginpage.getloginbutton().click()

        loginpage.getrequestotp().click()
        err_msg = loginpage.getotperror().text

        assert "ID/Mobile number" in err_msg
        print(err_msg)

    #TC 2
    def test_LoginwithNumber(self, getData):
        loginpage = LoginPage(self.driver)

        loginpage.getcrossmark().click()
        loginpage.getloginbutton().click()
        loginpage.getmobile().send_keys(getData["Mobile"])
        loginpage.getrequestotp().click()


    @pytest.fixture(params=LoginPageData.loginpage_data)
    def getData(self,request):
        return request.param


