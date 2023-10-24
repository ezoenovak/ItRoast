from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Data.links import MAIN_PAGE, LINKEDIN_PAGE, REG_PAGE
from Locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def check_reg_clickability(self):
        reg_link = self.driver.find_element(*MainPageLocators.REG_LINK)
        self.action_move_to_element(reg_link)
        self.element_is_clickable(reg_link)

    def linkedin_redirection_correct(self):
        self.find_element_and_click(MainPageLocators.LINKEDIN_LINK)
        self.assert_current_url(LINKEDIN_PAGE)

    def reg_redirection_correct(self):
        self.find_element_and_click(MainPageLocators.REG_LINK)
        self.assert_current_url(REG_PAGE)


