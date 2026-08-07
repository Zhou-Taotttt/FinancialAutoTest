import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config import BASE_URL
from tool import Tools


class PageRegister(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.phone=(By.ID,'phone')
        self.password=(By.ID,'password')
        self.img_code=(By.ID,'verifycode')
        self.get_phone_code=(By.ID,'get_phone_code')
        self.phone_code=(By.ID,'phone_code')
        self.reg=(By.CLASS_NAME,'lg-btn')
        self.success_result=(By.XPATH,'//*[text()="注册成功！"]')
        # 注册失败的弹框是toast提示，显示时间很短，所以定位就定位当前未跳转的页面元素即可
        self.fail_result=(By.CSS_SELECTOR,'#reg_form > div.reg-title')

    def open_url(self):
        self.driver.get(BASE_URL+'/common/member/reg')

    def register(self,phone,password,img_code,phone_code):
        self.base_input(self.phone,phone)
        self.base_input(self.password,password)
        self.base_input(self.img_code,img_code)
        self.base_click(self.get_phone_code)
        time.sleep(2)
        self.base_input(self.phone_code,phone_code)
        self.base_click(self.reg)
        time.sleep(3)

    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text

if __name__=='__main__':
    reg=PageRegister(Tools.get_driver())
    reg.open_url()
    reg.register('13800015138','123456a','8888','666666')
