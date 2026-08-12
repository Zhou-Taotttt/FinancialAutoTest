import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageCreditReview(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.loan_manger=(By.LINK_TEXT,'借款管理')
        self.quota_manger=(By.XPATH,'//span[text()="额度管理"]')
        self.quota_apply_review=(By.XPATH,'//*[@id="sidebar"]/ul/li[5]/ul/li[2]/a')
        # 额度申请审核表单在frame里,需切换frame
        self.frame1=(By.ID,'iframe_box')
        self.search_phone=(By.NAME,'member_name')
        self.search_btn=(By.CSS_SELECTOR,'.srcbtn')
        # 选择第一条
        self.select_first=(By.XPATH,'/html/body/div[2]/div[3]/table/tbody/tr[1]')
        # 点击审核
        self.review_btn=(By.XPATH,'/html/body/div[2]/div[2]/ul/li[1]/a/span')
        # 审核表单也是在frame里
        self.frame2=(By.ID,'xubox_iframe1')
        self.pass_btn=(By.CSS_SELECTOR,'body > div:nth-child(2) > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > label:nth-child(1) > input')
        self.note=(By.CSS_SELECTOR,'body > div:nth-child(2) > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > div > textarea')
        self.code=(By.NAME,'valicode')
        self.save_btn=(By.CSS_SELECTOR,'body > div:nth-child(2) > form > table > tbody > tr:nth-child(8) > td.profile-info-value.ng-scope > input.dybtn.dybtn-save')

        # 额度申请记录
        self.quota_apply_record=(By.LINK_TEXT,'额度申请记录')
        self.status=(By.CSS_SELECTOR,'body > div:nth-child(2) > div.src_box.ng-scope > div > ul > li:nth-child(2) > div > select')
        self.status_first=(By.CSS_SELECTOR,'body > div:nth-child(2) > div.info_list > table > tbody > tr:nth-child(1) > td.status')

    def menu_manager(self):
        self.base_click(self.loan_manger)
        self.base_click(self.quota_manger)
        self.base_click(self.quota_apply_review)

    def search_record(self,phone):
        self.base_switch_frame(self.frame1)
        self.base_input(self.search_phone,phone)
        self.base_click(self.search_btn)

    def select_record(self):
        time.sleep(1)
        self.base_click(self.select_first)
        self.base_click(self.review_btn)

    def review_pass(self,note,code):
        self.base_switch_frame(self.frame2)
        time.sleep(1)
        self.base_click(self.pass_btn)
        self.base_input(self.note,note)
        self.base_input(self.code,code)
        self.base_click(self.save_btn)

    def apply_record(self,phone,value):
        # 退出第一个frame，因为当审核保存后审核表单就自动消失了
        self.base_default_frame()
        self.base_click(self.quota_apply_record)
        # 额度申请记录表单也在frame里，并且和额度申请审核的frame一样
        self.base_switch_frame(self.frame1)
        self.base_input(self.search_phone,phone)
        self.base_select_list(self.status,value)
        self.base_click(self.search_btn)

    def get_success_result(self):
        # 使用强制等待，因为状态元素一直在，如果使用显示等待获取的状态可能不是最新状态
        time.sleep(1)
        return self.fd_element(self.status_first).text
