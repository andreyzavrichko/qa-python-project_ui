import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Конструктор")
class TestMain:

    @allure.title("Переход на таб «Соусы»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sauce_tab(self, driver):
        main = MainPage(driver)
        with allure.step("Кликнуть таб «Соусы»"):
            main.click_sauce_tab()
        with allure.step("Проверить, что таб активен"):
            assert main.sauce_tab_is_active()

    @allure.title("Переход на таб «Булки»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_bun_tab(self, driver):
        main = MainPage(driver)
        with allure.step("Переключиться на «Соусы», затем обратно на «Булки»"):
            main.click_sauce_tab()
            main.click_bun_tab()
        with allure.step("Проверить, что таб «Булки» активен"):
            assert main.bun_tab_is_active()

    @allure.title("Переход на таб «Начинки»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filling_tab(self, driver):
        main = MainPage(driver)
        with allure.step("Кликнуть таб «Начинки»"):
            main.click_filling_tab()
        with allure.step("Проверить, что таб активен"):
            assert main.filling_tab_is_active()

    @allure.title("Переход в конструктор по клику на «Конструктор» из ленты заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_constructor_from_order_feed(self, driver):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        with allure.step("Перейти в ленту заказов"):
            main.click_order_feed_button()
            order_feed.wait_order_feed_page()
        with allure.step("Кликнуть «Конструктор»"):
            main.click_constructor_button()
        with allure.step("Проверить переход на главную"):
            main.wait_burger_title()

    @allure.title("Переход в «Лента заказов» по клику на кнопку в хедере")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_order_feed(self, driver):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        with allure.step("Кликнуть «Лента Заказов»"):
            main.click_order_feed_button()
        with allure.step("Проверить открытие ленты заказов"):
            order_feed.wait_order_feed_page()
            assert order_feed.order_feed_title_is_visible()

    @allure.title("Попап с деталями ингредиента открывается по клику")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_popup_opens_on_click(self, driver):
        main = MainPage(driver)
        with allure.step("Кликнуть на первый ингредиент"):
            main.click_first_ingredient()
        with allure.step("Проверить появление попапа"):
            assert main.ingredient_popup_is_visible()

    @allure.title("Попап ингредиента закрывается кликом по крестику")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_popup_closes_on_cross_click(self, driver):
        main = MainPage(driver)
        with allure.step("Открыть попап ингредиента"):
            main.click_first_ingredient()
            assert main.ingredient_popup_is_visible()
        with allure.step("Закрыть попап кнопкой ×"):
            main.close_popup()
        with allure.step("Проверить, что попап закрыт"):
            assert main.popup_is_closed()

    @allure.title("Каунтер ингредиента увеличивается при добавлении в заказ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increments_on_add(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        with allure.step("Запомнить начальное значение каунтера"):
            counter_before = main.get_ingredient_counter()
        with allure.step("Добавить ингредиент в заказ drag-and-drop"):
            main.drag_ingredient_to_basket()
        with allure.step("Проверить увеличение каунтера"):
            counter_after = main.get_ingredient_counter()
            assert counter_after > counter_before

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logged_in_user_can_place_order(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        with allure.step("Добавить ингредиент и оформить заказ"):
            main.drag_ingredient_to_basket()
            main.click_place_order()
        with allure.step("Проверить появление номера заказа в попапе"):
            order_number = main.get_order_number_from_modal()
            assert order_number.isdigit() or len(order_number) > 0
