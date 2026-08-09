import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page.page_login import PageLogin
from tool import Tools


@pytest.fixture()
def browser():
    # path=r'D:\develop\Python\Python312\chromedriver.exe'
    # ser = Service(executable_path=path)
    # driver = webdriver.Chrome(service=ser)
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    driver=Tools.get_driver()
    yield driver
    driver.quit()

@pytest.fixture()
def login_conftest(browser):
    page_login=PageLogin(browser)
    page_login.open_url()
    return page_login