from playwright.sync_api import expect, Locator


class Base:

    def __init__(self, page):
        self.page = page

    @staticmethod
    def expect_element_to_be_visible(el: Locator, timeout: int = 60000):
        return expect(el).to_be_visible(timeout=timeout)
