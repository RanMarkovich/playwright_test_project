from playwright.sync_api import sync_playwright
from pytest import fixture

from browser_factory import BrowserFactory
from pages.login import Login
from pages.main import Main


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="env: local / qa / lab / prod"
    )


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
def page(browser):
    page = browser.new_page()
    page.goto('https://dashboard.oolo.io')
    return page


@fixture
def login_page(page):
    return Login(page)


@fixture
def main_page(page):
    return Main(page)
