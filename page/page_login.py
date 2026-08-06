# 封装页面

import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config import BASE_URL
from tool import Tools
# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法

class PageLogin(BasePage):
    def __init__(self, driver):
        # self.driver=Tools.get_driver()
        # 重写父类获取driver对象
        # 将Tools.get_driver()视为参数，外部传参时可以选择传其它的浏览器，否则使用默认的Tools.get_driver()返回的driver对象
        # super().__init__(Tools.get_driver())
        super().__init__(driver)
        # 页面实例属性
        self.username=(By.ID,'keywords')
        self.password=(By.ID,'password')
        self.login_btn=(By.ID,'login-btn')
        self.success_result=(By.CLASS_NAME,'a-link1')
        self.fail_result=(By.CSS_SELECTOR,'[ng-bind="loginErr"]')

    def open_url(self):
        self.driver.get(BASE_URL+'/common/member/login')

    def login(self,username,password):
        # *拆包
        # self.driver.find_element(*self.username).send_keys('13800001138')
        # self.driver.find_element(*self.password).send_keys('123456')
        # self.driver.find_element(*self.login_btn).click()

        # 显示等待查找元素的参数本身传的是元组，所以不用拆包
        # ele1=self.fd_element(self.username)
        # ele1.clear()
        # ele1.send_keys('13800001138')
        # ele2=self.fd_element(self.password)
        # ele2.clear()
        # ele2.send_keys('123456a')
        # self.fd_element(self.login_btn).click()
        self.base_input(self.username,username)
        self.base_input(self.password,password)
        self.base_click(self.login_btn)
        time.sleep(3)
    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text
# 调试
if __name__=='__main__':
    lg=PageLogin(Tools.get_driver())
    lg.open_url()
    lg.login('13800001138','123456a')