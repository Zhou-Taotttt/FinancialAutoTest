from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageOpenAccount(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.open=(By.LINK_TEXT,'立即开通')
        self.real_name=(By.NAME,'realname')
        self.card_id=(By.NAME,'card_id')
        self.submit=(By.CSS_SELECTOR,'[value="确认提交"]')
        self.open_acc=(By.CSS_SELECTOR,'.btn.ng-scope')
        self.success_result=(By.TAG_NAME,'body')

    def open_account(self,name,card):
        self.base_click(self.open)
        self.base_input(self.real_name,name)
        self.base_input(self.card_id,card)
        self.base_click(self.submit)
        self.base_click(self.open_acc)

    def get_success_result(self):
        # 成功结果在新窗口，要切换窗口定位元素
        ele=self.base_switch_handle(self.success_result)
        return ele.text