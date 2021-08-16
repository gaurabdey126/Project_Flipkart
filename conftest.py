import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\geckodriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.flipkart.com/")
    request.cls.driver = driver
    #
    # yield
    # driver.close()