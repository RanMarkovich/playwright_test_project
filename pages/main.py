from pages.base import Base


class Main(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @property
    def logged_in_successfully_banner(self):
        return self.page.locator('css=h1.post-title').filter(has_text='Logged In Successfully')
