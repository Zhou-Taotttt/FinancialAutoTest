from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageCreditApplication(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.role=(By.XPATH,'//*[text()="借款账户"]')
        self.apply_credit=(By.LINK_TEXT,'申请额度')
        self.money=(By.ID,'amount_account')
        self.detail=(By.NAME,'remark')
        self.code=(By.ID,'verifycode')
        self.submit=(By.CSS_SELECTOR,'.btn-submit.btn-md')
        self.apply_success=(By.XPATH,'//*[@id="amount_list"]/tr/td[3]')

    def switch_role(self):
        self.base_click(self.role)

    def click_apply(self):
        self.base_click(self.apply_credit)

    def credit_application(self,money,detail,code):
        self.base_input(self.money,money)
        self.base_input(self.detail,detail)
        self.base_input(self.code,code)
        self.base_click(self.submit)

    def get_success_result(self):
        return self.fd_element(self.apply_success).text
