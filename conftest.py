import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from Data.links import MAIN_PAGE


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquitting browser..")
    driver.quit()


@pytest.fixture()
def open_main_page(driver):
    driver.get(MAIN_PAGE)
    driver.maximize_window()
