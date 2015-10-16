__author__ = 'slaureano'


import unittest, time, base64, random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

username = base64.standard_b64decode("c2xhdXI=")
password = base64.standard_b64decode('RWFydGg3Nzc=')

class MyTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://qa.google.com/login'
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()


    def _wait_for_element(self, css_selector):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(lambda driver: self.driver.find_element_by_css_selector(css_selector).is_displayed())
            return True
        except:
            return False

    def random_amount(self, length):
        number = "0123456789"
        id = ""
        for i in range (0, length, 2):
            id += random.choice(number)
        return id


    def _do_login(self, username, password):
        username_css = "#username"
        password_css = "#password"


        submit_button_css = ".button.btn.btn-large"
        logged_in_username_css = ".dropdown-arrow.pull-right"

        self.driver.find_element_by_css_selector(username_css).send_keys(username)
        self.driver.find_element_by_css_selector(password_css).send_keys(password)
        self.driver.find_element_by_css_selector(submit_button_css).click()

        self._wait_for_element(logged_in_username_css)


    def test_funding_money_ach(self):

        self._do_login(username, password)

        logged_in_username_css = ".dropdown-arrow.pull-right"
        account_dropdown = self.driver.find_element_by_css_selector(logged_in_username_css)
        funding_button = self.driver.find_element_by_css_selector("#nav > li.dropdown-arrow.pull-right > ul > li:nth-child(2) > a")

        hover = ActionChains(self.driver).move_to_element(account_dropdown)
        hover.perform()
        #time.sleep(1000)

        funding_button.click()

        _expected_url = "https://qa.google.com/deposit"
        current_url = self.driver.current_url

        assert current_url == _expected_url, "CURRENT: {0}, EXPECTED: {1}".format(current_url, _expected_url)

        ach_button_css = "body > div.content-container-pattern > div.container.funding-container > div.funding-options-container > ul:nth-child(1) > li.hd.ach > a > div.btn.btn-large.btn-orange"

        self.driver.find_element_by_css_selector(ach_button_css).click()

        amount_box_css = "#amount"
        self.driver.find_element_by_css_selector(amount_box_css).send_keys(self.random_amount(4))
        submit_button_css= "#fund-ach-form > button"
        self.driver.find_element_by_css_selector(submit_button_css).click()
        ach_deposit_thanks_css = "body > div.content-container-pattern > div:nth-child(2) > div"
        time.sleep(10)
        assert self.driver.find_element_by_css_selector(ach_deposit_thanks_css).is_displayed()
        expected_complete_url = "https://qa.google.com/deposit"
        assert current_url == expected_complete_url, "CURRENT: {0}, EXPECTED: {1}".format(current_url, expected_complete_url)








