from pages.base import Base


class Main(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @property
    def welcome_banner(self):
        return self.page.get_by_text('Hi Ran!')
