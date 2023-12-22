from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_profile(self):
        profile_btn = self.browser.find_element(*MainPageLocators.PROFILE_BTN)
        profile_btn.click()

    def go_to_pet_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.PET_NAME)
        pet_name.send_keys('Sam')
        pet_name.click()

    def go_to_pet_type_cat(self):
        pet_type_cat = self.browser.find_element(*MainPageLocators.TYPE_SELECTOR)
        pet_type_cat.click()
        pet_type_cat = self.browser.find_element(*MainPageLocators.CAT)
        pet_type_cat.click()
