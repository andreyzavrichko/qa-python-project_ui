from pages.base_page import BasePage
from locators.register_locators import RegisterLocators


class RegisterPage(BasePage):

    def set_name(self, name: str):
        self.send_keys(RegisterLocators.NAME_INPUT, name)

    def set_email(self, email: str):
        self.send_keys(RegisterLocators.EMAIL_INPUT, email)

    def set_password(self, password: str):
        self.send_keys(RegisterLocators.PASSWORD_INPUT, password)

    def click_register_button(self):
        self.click(RegisterLocators.REGISTER_BUTTON)

    def click_login_link(self):
        self.click(RegisterLocators.LOGIN_LINK)

    def incorrect_password_error_text(self) -> str:
        return self.get_text(RegisterLocators.INCORRECT_PASSWORD_ERROR)