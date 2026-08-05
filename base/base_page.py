# 页面公共操作

import os.path

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from config import PATH
from tool import GetLog


class BasePage():
    def __init__(self,driver,timeout=10):
        self.driver=driver
        self.default_timeout=timeout

    def fd_element(self,loc):
        try:
            # element=WebDriverWait(self.driver,self.default_timeout).until(EC.visibility_of_element_located(loc))
            # 为确保切换frame时出错，改为presence_of_element_located，因为它只需要定位元素存在，不要求定位元素显示在页面，frame不显示在页面
            element=WebDriverWait(self.driver,self.default_timeout).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f'元素定位超时，定位信息:{loc},错误信息:{e}')
            raise
    def base_input(self,loc,text):
        ele=self.fd_element(loc)
        ele.clear()
        ele.send_keys(text)

    def base_click(self,loc):
        self.fd_element(loc).click()

    def get_shot(self,file_name):
        file_path=os.path.join(PATH,'img',file_name)
        self.driver.get_screenshot_as_file(file_path)

    def base_switch_handle(self,loc):
        WebDriverWait(self.driver,self.default_timeout).until(lambda x:len(x.window_handles)>1)
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        ele=self.fd_element(loc)
        return ele

    def base_switch_frame(self,loc):
        frame_ele=self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)

    def base_default_frame(self):
        self.driver.switch_to.default_content()

    def base_select_list(self,loc,value):
        select=Select(self.fd_element(loc))
        select.select_by_value(value)