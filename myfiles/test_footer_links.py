import unittest, time
from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://qa.google.com'
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


    def test_explore_stocks_link(self):

        _explore_css = 'div.span4:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)'
        _explore_stock_css = 'h1.page-title'
        _expected_result = "EXPLORE STOCKS"
        _expected_url = self.base_url +"/explore"


        wait = WebDriverWait(self.driver, 30)
        wait.until(lambda driver: self.driver.find_element_by_css_selector(_explore_css).is_displayed())

        self.driver.find_element_by_css_selector(_explore_css).click()

        actual_result = self.driver.find_element_by_css_selector(_explore_stock_css).text
        current_url = self.driver.current_url
        assert actual_result == _expected_result, "CURRENT: {0}, EXPECTED: {1}".format(actual_result, _expected_result)
        assert current_url == _expected_url, "CURRENT: {0}, EXPECTED: {1}".format(current_url, _expected_url)

        self.driver.back()


    def test_explore_stock_text(self):

        _explore_css = 'div.span4:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)'
        _expected_result = 'Explore Stocks'

        actual_result = self.driver.find_element_by_css_selector(_explore_css).text
        assert actual_result == _expected_result, "CURRENT: {0}, EXPECTED: {1}".format(actual_result, _expected_result)


    def test_explore_stock_color(self):

        _explore_css = 'div.span4:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)'
        _expected_result ='#0066cc'

        actual_color = self.driver.find_element_by_css_selector(_explore_css).value_of_css_property('color')

        actual_result = Color.from_string(actual_color).hex
        assert actual_result == _expected_result, "CURRENT: {0}, EXPECTED: {1}".format(actual_result, _expected_result)


    def test_learn_more(self):

        _learn_more_link_css = 'div.span4.offset1.footer-links-logos > div.hidden-phone > div.row-fluid.footer-links > div.span4 > ul > li:nth-child(2) > a'
        _overview_css = "body > div.content-container-pattern > div.hiw-container > div.container.hiw-overview-section > p.headline"
        _expected_result = "Overview"
        actual_result = self.driver.find_element_by_css_selector(_overview_css).text
        current_url = self.driver.current_url
        _expected_url = self.base_url +"/how-it-works"

        self.driver.find_element_by_css_selector(_learn_more_link_css).click()

        assert actual_result == _expected_result, actual_result
        assert current_url == _expected_url


    def test_home(self):

        help_css = 'div.span4.offset1.footer-links-logos > div.hidden-phone > div.row-fluid.footer-links > div.span4 > ul > li:nth-child(3) > a'
        most_popular_q__css = '#rn_PageContent > div > h2'
        expected_result = "MOST POPULAR QUESTIONS"
        expected_url = "https://google.custhelp.com/app/home"

        self.driver.find_element_by_css_selector(help_css).click()
        actual_result = self.driver.find_element_by_css_selector(most_popular_q__css).text
        assert actual_result == expected_result, actual_result
        current_url = self.driver.current_url
        self._wait_for_element(most_popular_q__css)
        assert current_url == expected_url, current_url

        popular_questions_css = '#rn_ProductCategoryList_main_3 > h2:nth-child(1) > div > a'
        actual_color = self.driver.find_element_by_css_selector(popular_questions_css).value_of_css_property('color')
        expected_color = '#c87100'
        actual_color_result = Color.from_string(actual_color).hex
        assert actual_color_result == expected_color, actual_color_result

    def test_about_google(self):

        about_google_css = 'div.span4.offset1.footer-links-logos > div.hidden-phone > div.row-fluid.footer-links > div.span4 > ul > li:nth-child(4) > a'
        about_us_css = 'body > div > div.hero-segment > div > section > div > div.section-header'
        expected_result = "ABOUT US"
        expected_url = self.base_url + "/about"

        self.driver.find_element_by_css_selector(about_google_css).click()
        actual_result= self.driver.find_element_by_css_selector(about_us_css).text
        assert actual_result == expected_result, actual_result
        current_url = self.driver.current_url
        self._wait_for_element(about_us_css)
        assert current_url == expected_url, current_url

    def test_press(self):

        press_css = 'div.span4.offset1.footer-links-logos > div.hidden-phone > div.row-fluid.footer-links > div.span4 > ul > li:nth-child(5) > a'
        press_releases_css = '#press_releases > a'
        expected_result = "PRESS RELEASES"
        expected_url = self.base_url + "/press"

        self.driver.find_element_by_css_selector(press_css).click()
        actual_result= self.driver.find_element_by_css_selector(press_releases_css).text
        assert actual_result == expected_result, actual_result
        current_url = self.driver.current_url
        self._wait_for_element(press_releases_css)
        assert current_url == expected_url, current_url

    def test_risk_modal_not_displayed(self):

        risk_modal_css = '#risk-modal-body'
        risk_modal = self.driver.find_element_by_css_selector(risk_modal_css)

        assert risk_modal.is_displayed() is False, risk_modal.is_displayed()



    def test_risk_modal_displayed(self):

        view_risks_css = 'div.row-fluid > div.span7.footer-copy > p:nth-child(5) > a'
        risk_modal_css = '#risk-modal-body'
        risk_modal = self.driver.find_element_by_css_selector(risk_modal_css)

        self.driver.find_element_by_css_selector(view_risks_css).click()
        assert risk_modal.is_displayed() is True





