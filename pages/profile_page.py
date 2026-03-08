from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


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

    def order_history_is_open(self) -> bool:
        return self.current_url_contains("/account/order-history")

    def click_logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)