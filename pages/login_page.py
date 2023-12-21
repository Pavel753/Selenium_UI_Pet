from .base_page import BasePage
from .locators import LoginPageLocators
from credentions import test_password, test_login


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(test_login)

    def go_to_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(test_password)

    def click_button(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()
