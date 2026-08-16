import pytest
from page.page_login import PageLogin
from script import log
from tool import Tools, read_json


class TestLogin:
    def setup_method(self):
        # 准备数据
        self.page_login = PageLogin(Tools.get_driver())
        # 打开网页
        self.page_login.open_url()

    def teardown_method(self):
        Tools.quit_driver()
    @pytest.mark.parametrize('phone,password,expect',read_json('login_data.json'))
    def test_login(self,phone,password,expect):
        # 输入信息
        self.page_login.login(phone,password)
        # 打印日志
        if expect==phone:
            result=self.page_login.get_success_result()
        else:
            result=self.page_login.get_fail_result()
        log.debug(f"登录结果：{result}")
        # 断言
        assert expect in result
