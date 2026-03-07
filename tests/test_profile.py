import allure
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_personal_area(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        profile = ProfilePage(driver)
        with allure.step("Кликнуть «Личный кабинет»"):
            main.click_personal_area()
        with allure.step("Проверить отображение страницы профиля"):
            profile.wait_profile_page()
            assert profile.profile_info_is_correct()

    @allure.title("Переход в «История заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_order_history(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        profile = ProfilePage(driver)
        with allure.step("Перейти в личный кабинет"):
            main.click_personal_area()
            profile.wait_profile_page()
        with allure.step("Кликнуть «История заказов»"):
            profile.click_order_history()
        with allure.step("Проверить открытие раздела"):
            assert profile.order_history_is_open()

    @allure.title("Выход из аккаунта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        auth = AuthPage(driver)
        profile = ProfilePage(driver)
        with allure.step("Перейти в личный кабинет"):
            main.click_personal_area()
            profile.wait_profile_page()
        with allure.step("Нажать «Выход»"):
            profile.click_logout()
        with allure.step("Проверить редирект на страницу входа"):
            auth.wait_auth_page()
            assert auth.auth_title_text() == "Вход"

    @allure.title("Переход из профиля в конструктор через кнопку «Конструктор»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_constructor_from_profile(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        profile = ProfilePage(driver)
        with allure.step("Перейти в личный кабинет"):
            main.click_personal_area()
            profile.wait_profile_page()
        with allure.step("Кликнуть «Конструктор»"):
            main.click_constructor_button()
        with allure.step("Проверить отображение конструктора"):
            main.wait_burger_title()
            assert main.burger_title_is_visible()

    @allure.title("Переход из профиля в конструктор через логотип")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_constructor_via_logo(self, authenticated_driver, driver):
        driver, user = authenticated_driver
        main = MainPage(driver)
        profile = ProfilePage(driver)
        with allure.step("Перейти в личный кабинет"):
            main.click_personal_area()
            profile.wait_profile_page()
        with allure.step("Кликнуть на логотип"):
            main.click_logo()
        with allure.step("Проверить отображение конструктора"):
            main.wait_burger_title()
            assert main.burger_title_is_visible()