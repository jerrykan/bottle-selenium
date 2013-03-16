from bottle import app
from selenium import webdriver

from .liveserver import LiveServerTestCase

import main


class SeleniumTest(LiveServerTestCase):
    def create_app(self):
        return app()

    def test_submit_form(self):
        driver = webdriver.Firefox()

        # Load index page
        driver.get(self.url_base())
        self.assertTrue('Useless Query' in driver.title)

        # Submit a query
        field = driver.find_element_by_id('query')
        field.send_keys('something')
        driver.find_element_by_id('submit').click()

        # Check the result
        self.assertTrue('Useless Query Result' in driver.title)

        body = driver.find_element_by_tag_name('body')
        self.assertTrue('You searched for "something".' in body.text)
        self.assertTrue('It was useless.' in body.text)

        driver.close()
