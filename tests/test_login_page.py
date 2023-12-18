from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.click_button()
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, '//*[@id="app"]/header/div/ul/li[1]/a/span[2]')
    browser.save_screenshot('result6.png')
