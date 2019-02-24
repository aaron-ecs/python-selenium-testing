from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def browser_firefox(context):
    context.driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={
            'browserName': 'firefox',
            'javascriptEnabled': True
        })
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(browser_firefox, context)
