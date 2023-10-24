from selenium.webdriver.common.by import By

class MainPageLocators:

    REG_LINK = (By.CSS_SELECTOR, "[href='/auth']")
    LINKEDIN_LINK = (By.CSS_SELECTOR, "[alt='linkedin']")