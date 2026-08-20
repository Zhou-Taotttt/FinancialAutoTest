from page.page_back_login import PageBackLogin
from script import log
from tool import Tools


class TestBackLogin:
    def setup_method(self):
        driver=Tools.get_driver()
        self.page_back_login=PageBackLogin(driver)
        self.page_back_login.open_url()

    def teardown_method(self):
        self.page_back_login.get_shot('back_login.png')
        Tools.quit_driver()

    def test_back_login(self):
        try:
            self.page_back_login.back_login('test_admin','test_password','0000')
            result=self.page_back_login.get_success_result()
            log.info(f'登录成功结果：'+result)
            assert 'test_admin' in result
        except Exception as e:
            log.info(f'登录错误结果：'+e)
            raise
