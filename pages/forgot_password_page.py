from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    def wait_forgot_password_page(self):
        self.wait_visible(ForgotPasswordLocators.FORGOT_PASSWORD_TITLE)

    def forgot_password_title_is_visible(self) -> bool:
        return self.is_displayed(ForgotPasswordLocators.FORGOT_PASSWORD_TITLE)

    def set_email(self, email: str):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)

    def click_show_hide_password(self):
        self.click(ForgotPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    def click_login_link(self):
        self.click(ForgotPasswordLocators.LOGIN_LINK)

    def password_input_is_active(self) -> bool:
        cls = self.get_attribute(
            ForgotPasswordLocators.PASSWORD_INPUT_CONTAINER,
            "class"
        )
        return "input_status_active" in cls

    def reset_password_page_is_open(self) -> bool:
        return self.current_url_contains("/forgot-password")