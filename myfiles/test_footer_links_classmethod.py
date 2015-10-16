import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://qa.google.com')


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def test_explore_stocks_link(self):

        _explore_css = 'div.span4:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)'
        _explore_stock_css = 'h1.page-title'
        _expected_result = "EXPLORE STOCKS"


        # wait = WebDriverWait(self.driver, 30)
        # wait.until(lambda driver: self.driver.find_element_by_css_selector(_explore_css).is_displayed())

        self.driver.find_element_by_css_selector(_explore_css).click()

        actual_result = self.driver.find_element_by_css_selector(_explore_stock_css).text
        assert actual_result == _expected_result, "CURRENT: {0}, EXPECTED: {1}".format(actual_result, _expected_result)
        self.driver.back()


    def test_explore_stock_text(self):

        _explore_css = 'div.span4:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)'
        _expected_result = 'Explore Stocks'

        actual_result = self.driver.find_element_by_css_selector(_explore_css).text
        assert actual_result == _expected_result, "CURRENT: {0}, EXPECTED: {1}".format(actual_result, _expected_result)





