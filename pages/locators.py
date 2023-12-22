from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    PROFILE_BTN = (By.CSS_SELECTOR, '.p-menuitem-text')
    TYPE_SELECTOR = (By.ID, 'typesSelector')
    DOG = (By.XPATH, '//div[3]/div/ul/li[1]')
    CAT = (By.XPATH, '//div[3]/div/ul/li[2]')
    REPTILE = (By.XPATH, '//div[3]/div/ul/li[3]')
    HAMSTER = (By.XPATH, '//div[3]/div/ul/li[4]')
    PARROT = (By.XPATH, '//div[3]/div/ul/li[5]')
    PET_NAME = (By.ID, 'petName')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class RegisterPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_CONFIRM_PASS = (By.CSS_SELECTOR, '#confirm_password > input')
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    ADD_PET = (By.CSS_SELECTOR, '.pi-plus')
    DELETE_PROFILE = (By.CSS_SELECTOR, '.col-6:nth-child(2) > .p-button')
    DELETE_PROFILE_YES = (By.XPATH, '//div[3]/div[2]/button[2]')
    DELETE_PROFILE_NO = (By.XPATH, '//div[3]/div[2]/button[1]')
    NAME = (By.ID, 'name')
    TYPE = (By.ID, 'typeSelector')
    DOG = (By.XPATH, '//div[3]/div/ul/li[1]')
    CAT = (By.XPATH, '//div[3]/div/ul/li[2]')
    REPTILE = (By.XPATH, '//div[3]/div/ul/li[3]')
    HAMSTER = (By.XPATH, '//div[3]/div/ul/li[4]')
    PARROT = (By.XPATH, '//div[3]/div/ul/li[5]')
    AGE = (By.CSS_SELECTOR, '#age > input')
    GENDER = (By.ID, 'genderSelector')
    MALE = (By.XPATH, '//div[3]/div/ul/li[1]')
    FEMALE = (By.XPATH, '//div[3]/div/ul/li[2]')
    SUBMIT = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CANCEL = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[2]')
    EDIT_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div/div/div[2]/button[1]')
    DELETE_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div/div/div[2]/button[2]')
    SAVE = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')
    DELETE_PET_YES = (By.XPATH, '//div[3]/div[2]/button[2]')
    DELETE_PET_NO = (By.XPATH, '//div[3]/div[2]/button[1]')
