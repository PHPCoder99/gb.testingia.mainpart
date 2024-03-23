import yaml
from selenium.webdriver.common.by import By

from TestPage import TestPage

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    testpage = TestPage(browser)
    testpage.go_to_site()
    testpage.enter_keys((By.XPATH, testdata["locator_username"]), testdata["username"])
    testpage.enter_keys((By.XPATH, testdata["locator_password"]), testdata["password"])
    testpage.click_btn((By.XPATH, testdata["locator_login_btn"]))
    testpage.click_btn((By.XPATH, testdata["locator_about"]))
    assert testpage.get_element_property((By.XPATH, testdata["locator_heading"]), "font-size") == "32px"
