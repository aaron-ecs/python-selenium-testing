"""
Test script for searching within a given website on Google
"""
from behave import given, when, then
from test.features.steps.google_page import GooglePage


def before_all(context):
    context.driver.get("http://www.google.com")


@given('I want to find {term} within website {website}')
def build_search(context, term, website):
    """ Build the search query from the feature scenario """
    context.search_term = "site:%s %s" % (website, term)
    context.website = website


@when('I search on {website}')
def perform_search(context, website):
    """ Enter the search term and search """
    context.execute_steps('''when I want to invoke another step''')
    context.google_page = GooglePage(context.driver)
    context.google_page.search(context.search_term)


@when('I want to invoke another step')
def do_magic_things(context):
    context.driver.get("http://www.google.co.uk")


@then('{term} is included in the results')
def check_results(context, term):
    """ Check the first 2 results are to the given web domain """
    for url in context.google_page.check_results():
        assert context.website in url
