import pytest
import time
from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.with_registration
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    browser.set_window_size(1200, 800)
    page.go_to_login_page()
    browser.save_screenshot('result5.png')


@pytest.mark.regression
def test_go_to_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_pet_name()
    page.go_to_pet_type_cat()
