from page.page_back_login import PageBackLogin
from page.page_credit_review import PageCreditReview
from script import log
from tool import Tools


class TestCreditReview:
    def setup_method(self):
        driver=Tools.get_driver()
        self.back_login=PageBackLogin(driver)
        self.back_login.open_url()
        self.back_login.back_login('test_admin','test_password','0000')

        self.credit_review=PageCreditReview(driver)
        self.credit_review.menu_manager()
        self.credit_review.search_record('13800001001')
        self.credit_review.select_record()

    def teardown_method(self):
        self.credit_review.get_shot('credit_review_success.png')
        Tools.quit_driver()

    def test_01_credit_review_success(self):
        self.credit_review.review_pass('审核通过','0000')
        self.credit_review.apply_record('13800001001','0')
        result=self.credit_review.get_success_result()
        log.info(result)
        assert '通过' == result
