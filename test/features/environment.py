from behave import fixture, use_fixture
from selenium import webdriver

BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


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
    setup_debug_on_error(context.config.userdata)
    use_fixture(browser_firefox, context)


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)
