import pytest
from pages.profile_page import ProfilePage
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.with_registration
def test_go_to_add_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet()
    page.go_to_name()
    page.go_to_type_cat()
    page.go_to_age()
    page.go_to_gender_male()
    page.go_to_submit()


@pytest.mark.regression
@pytest.mark.with_registration
def test_go_to_edit_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet()
    time.sleep(1)
    page.go_to_gender_female()
    page.go_to_type_reptile()
    page.go_to_save_edit_pet()


@pytest.mark.regression
@pytest.mark.with_registration
def test_go_to_delete_pet_no(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_pet()
    page.go_to_delete_pet_no()


@pytest.mark.regression
@pytest.mark.with_registration
def test_go_delete_pet_yes(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_pet()
    page.go_to_delete_pet_yes()


@pytest.mark.regression
@pytest.mark.with_registration
def test_go_to_delete_profile_no(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_profile()
    page.go_to_delete_profile_no()


@pytest.mark.skip
@pytest.mark.regression
@pytest.mark.with_registration
def test_go_to_delete_profile_yes(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_profile()
    page.go_to_delete_profile_yes()
