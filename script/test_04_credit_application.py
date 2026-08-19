from page.page_credit_application import PageCreditApplication
from page.page_login import PageLogin
from script import log
from tool import Tools


class TestCreditApplication:
    def setup_method(self):
        driver=Tools.get_driver()
        self.page_credit_application=PageCreditApplication(driver)
        self.page_login=PageLogin(driver)
        self.page_login.open_url()
        self.page_login.login('13800010138','123456a')

    def teardown_method(self):
        Tools.quit_driver()

    def test_01_credit_application_success(self):
        try:
            self.page_credit_application.switch_role()
            self.page_credit_application.click_apply()
            self.page_credit_application.credit_application("10000","测试信息",'8888')
            result=self.page_credit_application.get_success_result()
            log.info(f"额度申请成功结果："+result)
            assert '10,000.00'==result
        except Exception as e:
            log.info(f"额度申请失败结果："+e)
            raise