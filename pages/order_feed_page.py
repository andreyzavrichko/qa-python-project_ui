from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    def wait_order_feed_page(self):
        self.wait_visible(OrderFeedLocators.ORDER_FEED_TITLE)

    def order_feed_title_is_visible(self) -> bool:
        return self.is_displayed(OrderFeedLocators.ORDER_FEED_TITLE)

    def click_first_order(self):
        self.click(OrderFeedLocators.FIRST_ORDER_ITEM)

    def order_details_modal_is_visible(self) -> bool:
        return self.is_displayed(OrderFeedLocators.ORDER_DETAILS_MODAL)

    def get_all_order_numbers_in_feed(self) -> list[str]:
        items = self.find_all(OrderFeedLocators.ORDER_ITEM_NUMBER)
        return [item.text for item in items]

    def get_done_all_time_counter(self) -> int:
        text = self.get_text(OrderFeedLocators.DONE_ALL_TIME_COUNTER)
        return int(text.replace(" ", ""))

    def get_done_today_counter(self) -> int:
        text = self.get_text(OrderFeedLocators.DONE_TODAY_COUNTER)
        return int(text.replace(" ", ""))


    def order_number_in_progress(self, order_number: str) -> bool:
        WebDriverWait(self.driver, 10).until(
            lambda d: any(
                order_number in el.text
                for el in self.find_all(OrderFeedLocators.IN_PROGRESS_ORDER_NUMBER)
            )
        )
        return True
