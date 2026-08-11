from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config import BACK_URL


class PageBackLogin(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username=(By.ID,'username')
        self.password=(By.ID,'password')
        self.code=(By.ID,'valicode')
        self.login_btn=(By.CSS_SELECTOR,'[value="登录"]')
        self.success_result=(By.XPATH,'/html/body/div[1]/div[3]/ul/li[2]/a/span')

    def open_url(self):
        self.driver.get(BACK_URL)

    def back_login(self,username,password,code):
        self.base_input(self.username,username)
        self.base_input(self.password,password)
        self.base_input(self.code,code)
        self.base_click(self.login_btn)

    def get_success_result(self):
        return self.fd_element(self.success_result).text