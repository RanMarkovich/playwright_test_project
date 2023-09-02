from playwright.sync_api import sync_playwright
from pytest import fixture, hookimpl

from browser_factory import BrowserFactory
from network_listener import NetworkListener
from pages.login import Login
from pages.main import Main


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="env: local / qa / lab / prod"
    )


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """helper method so request.node.rep_call.failed can be extracted on test teardown"""
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@fixture
def env(request):
    return request.config.getoption("--env")


@fixture
def browser(env):
    with sync_playwright() as p:
        browser = BrowserFactory(p, env).get_browser()
        yield browser
        browser.close()


@fixture
def page(request, browser):
    page = browser.new_page()
    NetworkListener(page).subscribe_to_network_traffic()
    page.goto('https://practicetestautomation.com/practice-test-login/')
    yield page
    try:
        if request.node.rep_call.failed:
            test_name = request.node.name
            page.screenshot(path=f"{test_name}.png", full_page=True)
    except Exception as e:
        print(f'failed to take screenshot - got error : {e}')


@fixture
def login_page(page):
    return Login(page)


@fixture
def main_page(page):
    return Main(page)
