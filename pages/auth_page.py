from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class AuthPage(BasePage):

    def wait_auth_page(self):
        self.wait_visible(AuthLocators.AUTH_TITLE)

    def auth_title_text(self) -> str:
        return self.get_text(AuthLocators.AUTH_TITLE)

    def set_email(self, email: str):
        self.send_keys(AuthLocators.EMAIL_INPUT, email)

    def set_password(self, password: str):
        self.send_keys(AuthLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(AuthLocators.LOGIN_BUTTON)

    def click_register_link(self):
        self.click(AuthLocators.REGISTER_LINK)

    def click_forgot_password_link(self):
        self.click(AuthLocators.FORGOT_PASSWORD_LINK)

    def login(self, email: str, password: str):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
