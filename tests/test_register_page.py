import pytest

from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_register(browser):
    link = 'http://34.141.58.52:8080/#/register'
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_confirm_password()
    page.click_button()
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    browser.save_screenshot('result7.png')
