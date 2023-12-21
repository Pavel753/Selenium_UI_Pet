from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def go_to_add_pet(self):
        add_pet = self.browser.find_element(*ProfilePageLocators.ADD_PET)
        add_pet.click()

    def go_to_delete_profile(self):
        delete_profile = self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE)
        delete_profile.click()

    def go_to_delete_profile_yes(self):
        delete_profile_yes = self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_YES)
        delete_profile_yes.click()

    def go_to_delete_profile_no(self):
        delete_profile_no = self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_NO)
        delete_profile_no.click()

    def go_to_name(self):
        name = self.browser.find_element(*ProfilePageLocators.NAME)
        name.send_keys('Найт')

    def go_to_type_dog(self):
        type1 = self.browser.find_element(*ProfilePageLocators.TYPE)
        type1.click()
        type1 = self.browser.find_element(*ProfilePageLocators.DOG)
        type1.click()

    def go_to_type_cat(self):
        type2 = self.browser.find_element(*ProfilePageLocators.TYPE)
        type2.click()
        type2 = self.browser.find_element(*ProfilePageLocators.CAT)
        type2.click()

    def go_to_type_reptile(self):
        type3 = self.browser.find_element(*ProfilePageLocators.TYPE)
        type3.click()
        type3 = self.browser.find_element(*ProfilePageLocators.REPTILE)
        type3.click()

    def go_to_type_hamster(self):
        type4 = self.browser.find_element(*ProfilePageLocators.TYPE)
        type4.click()
        type4 = self.browser.find_element(*ProfilePageLocators.HAMSTER)
        type4.click()

    def go_to_type_parrot(self):
        type5 = self.browser.find_element(*ProfilePageLocators.TYPE)
        type5.click()
        type5 = self.browser.find_element(*ProfilePageLocators.PARROT)
        type5.click()

    def go_to_age(self):
        age = self.browser.find_element(*ProfilePageLocators.AGE)
        age.send_keys('3')

    def go_to_gender_male(self):
        gender = self.browser.find_element(*ProfilePageLocators.GENDER)
        gender.click()
        gender = self.browser.find_element(*ProfilePageLocators.MALE)
        gender.click()

    def go_to_gender_female(self):
        gender = self.browser.find_element(*ProfilePageLocators.GENDER)
        gender.click()
        gender = self.browser.find_element(*ProfilePageLocators.FEMALE)
        gender.click()

    def go_to_submit(self):
        submit = self.browser.find_element(*ProfilePageLocators.SUBMIT)
        submit.click()

    def go_to_cancel(self):
        cancel = self.browser.find_element(*ProfilePageLocators.CANCEL)
        cancel.click()

    def go_to_delete_pet(self):
        delete = self.browser.find_element(*ProfilePageLocators.DELETE_PET)
        delete.click()

    def go_to_edit_pet(self):
        edit = self.browser.find_element(*ProfilePageLocators.EDIT_PET)
        edit.click()

    def go_to_save_edit_pet(self):
        save = self.browser.find_element(*ProfilePageLocators.SAVE)
        save.click()

    def go_to_delete_pet_no(self):
        delete_pet_no = self.browser.find_element(*ProfilePageLocators.DELETE_PET_NO)
        delete_pet_no.click()

    def go_to_delete_pet_yes(self):
        delete_pet_yes = self.browser.find_element(*ProfilePageLocators.DELETE_PET_YES)
        delete_pet_yes.click()
