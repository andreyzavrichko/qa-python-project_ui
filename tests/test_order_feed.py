import allure
from helpers.api_client import ApiClient
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Попап с деталями заказа открывается по клику на заказ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_details_popup_opens_on_click(self, driver):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        with allure.step("Перейти в ленту заказов"):
            main.click_order_feed_button()
            order_feed.wait_order_feed_page()
        with allure.step("Кликнуть на первый заказ"):
            order_feed.click_first_order()
        with allure.step("Проверить появление попапа с деталями"):
            assert order_feed.order_details_modal_is_visible()

    @allure.title("Заказы из «Истории заказов» отображаются в «Ленте заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_orders_appear_in_order_feed(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        profile = ProfilePage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Создать заказ через API"):
            ingredients = ApiClient.get_ingredients()
            bun_id = next(i["_id"] for i in ingredients if i["type"] == "bun")
            order = ApiClient.create_order(user["access_token"], [bun_id, bun_id])
            order_number = str(order["order"]["number"])

        with allure.step("Открыть историю заказов пользователя"):
            main.click_personal_area()
            profile.wait_profile_page()
            profile.click_order_history()

        with allure.step("Проверить наличие заказа в истории"):
            assert any(
                order_number in item.text
                for item in profile.order_history_items()
            )

        with allure.step("Перейти в ленту заказов"):
            main.click_order_feed_button()
            order_feed.wait_order_feed_page()

        with allure.step("Проверить, что заказ есть в ленте"):
            feed_numbers = order_feed.get_all_order_numbers_in_feed()
            assert any(order_number in n for n in feed_numbers)

    @allure.title("Счётчик «Выполнено за всё время» увеличивается после создания заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_time_counter_increments_after_order(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Открыть ленту и запомнить счётчик"):
            main.click_order_feed_button()
            order_feed.wait_order_feed_page()
            counter_before = order_feed.get_done_all_time_counter()

        with allure.step("Создать заказ через API"):
            ingredients = ApiClient.get_ingredients()
            bun_id = next(i["_id"] for i in ingredients if i["type"] == "bun")
            ApiClient.create_order(user["access_token"], [bun_id, bun_id])

        with allure.step("Обновить страницу и проверить счётчик"):
            driver.refresh()
            order_feed.wait_order_feed_page()
            counter_after = order_feed.get_done_all_time_counter()
            assert counter_after > counter_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после создания заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_today_counter_increments_after_order(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Открыть ленту и запомнить счётчик"):
            main.click_order_feed_button()
            order_feed.wait_order_feed_page()
            counter_before = order_feed.get_done_today_counter()

        with allure.step("Создать заказ через API"):
            ingredients = ApiClient.get_ingredients()
            bun_id = next(i["_id"] for i in ingredients if i["type"] == "bun")
            ApiClient.create_order(user["access_token"], [bun_id, bun_id])

        with allure.step("Обновить страницу и проверить счётчик"):
            driver.refresh()
            order_feed.wait_order_feed_page()
            counter_after = order_feed.get_done_today_counter()
            assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_new_order_number_appears_in_progress(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Создать заказ через API"):
            ingredients = ApiClient.get_ingredients()
            bun_id = next(i["_id"] for i in ingredients if i["type"] == "bun")
            order = ApiClient.create_order(user["access_token"], [bun_id, bun_id])
            order_number = str(order["order"]["number"])

        with allure.step("Открыть ленту заказов"):
            main.click_order_feed_button()
            order_feed.wait_order_feed_page()

        with allure.step(f"Проверить наличие #{order_number} в разделе «В работе»"):
            assert order_feed.order_number_in_progress(order_number)
