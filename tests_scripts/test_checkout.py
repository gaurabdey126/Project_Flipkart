import time
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from utilities.baseClass import BaseClass
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_verification_page import CartVerifyPage
from test_data.LoginPageData import LoginPageData


class Test_Checkout(BaseClass):

    @allure.severity(severity_level="HIGH")
    def test_checkout_single_product(self, getData):
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        productlistpage = ProductListPage(self.driver)
        productdetailspage = ProductDetailsPage(self.driver)
        cartverifypage = CartVerifyPage(self.driver)

        ## Login
        loginpage.getcross_mark().click()
        loginpage.getlogin_btn().click()
        loginpage.getenter_mobile().send_keys(getData["Mobile"])
        loginpage.getenter_pwd().send_keys(getData["Pwd"])
        loginpage.getsubmit_btn().click()
        time.sleep(3)

        ## Search
        homepage.getsearch_field().send_keys("Realme 8", Keys.ENTER)  ##this is the way of using Enter button

        i=-1
        for prod in productlistpage.getprod_name():
            i=i+1
            if prod.text == "realme 8 (Cyber Silver, 128 GB)":
                # print(prod.text)
                # print(productlistpage.getprod_details()[i].text)
                if "8 GB RAM" in (productlistpage.getprod_details()[i].text):
                    print(prod.text)
                    print(productlistpage.getprod_details()[i].text)
                    productlistpage.getprod_details()[i].click()

        self.driver.window_handles
        prod_list_window = self.driver.window_handles[0]
        prod_detail_window = self.driver.window_handles[1]

        self.driver.switch_to.window(prod_detail_window)

        productdetailspage.getadd_to_cart().click()

        ## Increase and Decrease
        time.sleep(3)
        try:
            (cartverifypage.getinrease_item().click())*2
        except Exception:
            pass
        print(cartverifypage.gettotal_amount().text)

        time.sleep(3)
        cartverifypage.getdecrease_item().click()
        print(cartverifypage.gettotal_amount().text)

        ## Remove popup
        cartverifypage.getremove().click()
        time.sleep(2)
        cartverifypage.getalert_cancel().click()

        time.sleep(2)
        cartverifypage.getremove().click()
        time.sleep(3)
        cartverifypage.getalert_remove().click()

        ## LOGOUT
        self.get_hover(loginpage.getmy_account())
        loginpage.getlogout().click()
        assert "Login" in (loginpage.getlogin_btn().text)
        print("Logged out SUCCESSFULLY")























    @pytest.fixture(params=LoginPageData.loginpage_data)
    def getData(self, request):
        return request.param
