from bottle import app
from selenium import webdriver

from .liveserver import LiveServerTestCase

# required to load the routes
import main


class SeleniumTest(LiveServerTestCase):
    def create_app(self):
        return app()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_submit_form(self):
        # Load index page
        self.driver.get(self.url_base())
        self.assertTrue('Useless Query' in self.driver.title)

        # Submit a query
        field = self.driver.find_element_by_id('query')
        field.send_keys('something')
        self.driver.find_element_by_id('submit').click()

        # Check the result
        self.assertTrue('Useless Query Result' in self.driver.title)

        body = self.driver.find_element_by_tag_name('body')
        self.assertTrue('You searched for "something".' in body.text)
        self.assertTrue('It was useless.' in body.text)
