from page.page_login import PageLogin
from script import log
from tool import Tools


class TestLogin:
    # def setup_method(self):
    #     # 准备数据
    #     self.page_login = PageLogin(Tools.get_driver())
    #     # 打开网页
    #     self.page_login.open_url()
    #
    # def teardown_method(self):
    #     Tools.quit_driver()

    # 将登录也封装在conftest中
    def test_01_login_success(self,login_conftest):
        # 输入信息
        login_conftest.login('13800001138','123456a')
        # 打印日志
        result=login_conftest.get_success_result()
        log.info(result)
        # 断言
        assert '13800001138'==result

    # 只封装调用浏览器在conftest中
    def test_02_login_fail_pwd_error(self,browser):
        # 准备数据
        self.page_login = PageLogin(browser)
        # 打开网页
        self.page_login.open_url()
        self.page_login.login('13800001138','123456')
        result=self.page_login.get_fail_result()
        log.info(result)
        assert '密码错误' in result
