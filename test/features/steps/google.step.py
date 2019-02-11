"""
Test script for searching within a given website on Google
"""
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

DRIVER = None
SEARCH_TERM = None
WEBSITE = None


@given('I want to find {term} within website {website}')
def build_search(self, term, website):
    """ Build the search query from the feature scenario """
    self.DRIVER = self.driver = webdriver.Remote(
        command_executor='http://zalenium:4444/wd/hub',
        desired_capabilities={
            'browserName': 'firefox',
            'javascriptEnabled': True
        })
    self.SEARCH_TERM = "site:%s %s" % (website, term)
    self.WEBSITE = website


@when('I search on Google')
def perform_search(self):
    """ Enter the search term and search """
    self.DRIVER.get("http://www.google.com")
    self.DRIVER.find_element_by_name('q').send_keys(self.SEARCH_TERM + Keys.ENTER)


@then('the results are returned')
def check_results(self):
    """ Check the first 2 results are to the given web domain """
    WebDriverWait(self.DRIVER, 5).until(
        lambda driver: self.DRIVER.find_elements_by_class_name("r"))
    results = self.DRIVER.find_elements_by_class_name("r")
    for result in results[:2]:
        assert self.WEBSITE in result.find_element_by_tag_name("a").get_attribute("href")
    self.DRIVER.quit()
