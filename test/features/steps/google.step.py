"""
Test script for searching within a given website on Google
"""
from behave import given, when, then
from test.features.steps.google_page import GooglePage


@given('I want to find {term} within website {website}')
def build_search(context, term, website):
    """ Build the search query from the feature scenario """
    context.search_term = "site:%s %s" % (website, term)
    context.website = website


@when('I search on Google')
def perform_search(context):
    context.google_page = GooglePage(context.driver)
    """ Enter the search term and search """
    context.driver.get("http://www.google.com")
    context.google_page.search(context.search_term)


@then('the results are returned')
def check_results(context):
    """ Check the first 2 results are to the given web domain """
    for url in context.google_page.check_results():
        assert context.website in url
