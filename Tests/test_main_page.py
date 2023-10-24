from Pages.main_page import MainPage


class TestMainPage:

    def test_can_click_reg(self, driver, open_main_page):
        page = MainPage(driver)
        page.check_reg_clickability()

    # Этот падает, потому что редирект не ведет куда надо
    def test_linkedin_redirection_correct(self, driver, open_main_page):
        page = MainPage(driver)
        page.linkedin_redirection_correct()

    # Этот проходит
    def test_reg_redirection_correct(self, driver, open_main_page):
        page = MainPage(driver)
        page.reg_redirection_correct()
