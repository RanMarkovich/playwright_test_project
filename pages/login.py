from pages.base import Base


class Login(Base):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @property
    def email_field(self):
        return self.page.wait_for_selector('[name="email"]')

    @property
    def password_field(self):
        return self.page.wait_for_selector('[name="password"]')

    @property
    def submit_btn(self):
        return self.page.wait_for_selector('[type=submit]')

    def submit_login_form(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.submit_btn.click()