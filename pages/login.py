from pages.base import Base


class Login(Base):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @property
    def username_field(self):
        return self.page.wait_for_selector('[id="username"]')

    @property
    def password_field(self):
        return self.page.wait_for_selector('[id="password"]')

    @property
    def submit_btn(self):
        return self.page.wait_for_selector('[id="submit"]')

    @property
    def invalid_username_banner(self):
        return self.page.locator('[id="error"]')

    def submit_login_form(self, email: str, password: str):
        self.username_field.fill(email)
        self.password_field.fill(password)
        self.submit_btn.click()