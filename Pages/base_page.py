from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element_and_click(self, locator):
        self.driver.find_element(*locator).click()

    def assert_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL does not match. Actual page is: {current_url}"

