from page.page_register import PageRegister
from script import log
from tool import Tools


class TestRegister:
    def setup_method(self):
        self.page_reg=PageRegister(Tools.get_driver())
        self.page_reg.open_url()

    def teardown_method(self):
        Tools.quit_driver()

    def test_01_register_success(self):
        self.page_reg.register('13800018138','123456a','8888','666666')
        result=self.page_reg.get_success_result()
        log.info(result)
        assert '注册成功' in result

    def test_02_register_fail_phone_exist(self):
        self.page_reg.register('13800017138', '123456a', '8888', '666666')
        result = self.page_reg.get_fail_result()
        log.info(result)
        assert '注册' in result