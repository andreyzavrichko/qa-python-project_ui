from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
from locators.auth_locators import AuthLocators
from locators.main_locators import MainLocators


class ProfilePage(BasePage):

    def wait_profile_page(self):
        self.wait_visible(ProfileLocators.PROFILE_INFO_TEXT)

    def profile_info_text(self) -> str:
        return self.get_text(ProfileLocators.PROFILE_INFO_TEXT)

    def profile_info_is_correct(self) -> bool:
        return "изменить свои персональные данные" in self.profile_info_text()

    def click_order_history(self):
        self.click(ProfileLocators.ORDER_HISTORY_LINK)

    def order_history_items(self):
        self.wait_visible(ProfileLocators.ORDER_HISTORY_ITEM)
        return self.find_all(ProfileLocators.ORDER_HISTORY_ITEM)

    def click_logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def wait_auth_page(self):
        self.wait_visible(AuthLocators.AUTH_TITLE)

    def auth_title_text(self) -> str:
        return self.get_text(AuthLocators.AUTH_TITLE)

    def burger_title_is_visible(self) -> bool:
        return self.is_displayed(MainLocators.BURGER_TITLE)
