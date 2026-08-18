from config import *
from page.page_login import PageLogin
from page.page_open_account import PageOpenAccount
from script import log
from tool import Tools


class TestOpenAccount:
    def setup_method(self):
        driver=Tools.get_driver()
        self.page_open_account=PageOpenAccount(driver)
        self.page_login=PageLogin(driver)
        self.page_login.open_url()
        self.page_login.login('13800011138','123456a')

    def teardown_method(self):
        Tools.quit_driver()

    def test_01_open_success(self):
        # 利用faker生成
        self.page_open_account.open_account(NAME,CARD)
        result=self.page_open_account.get_success_result()
        log.info(result)
        assert 'UserRegister OK'==result
