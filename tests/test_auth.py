import allure

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


@allure.feature("Авторизация")
class TestAuth:

    @allure.title("Авторизация через кнопку «Личный кабинет»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_via_personal_area_button(self, driver, new_user):
        main = MainPage(driver)
        with allure.step("Кликнуть на «Личный кабинет»"):
            main.click_personal_area()
        with allure.step("Ввести email и пароль, нажать «Войти»"):
            main.login(new_user["email"], new_user["password"])
        with allure.step("Кликнуть на «Личный кабинет» после входа"):
            main.click_personal_area()
        with allure.step("Проверить отображение профиля"):
            main.wait_profile_text()
            assert main.profile_text_is_correct()

    @allure.title("Авторизация через кнопку «Войти в аккаунт» на главной")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_via_main_login_button(self, driver, new_user):
        main = MainPage(driver)
        with allure.step("Кликнуть «Войти в аккаунт»"):
            main.click_login_order_button()
        with allure.step("Авторизоваться"):
            main.login(new_user["email"], new_user["password"])
        with allure.step("Перейти в профиль и проверить"):
            main.click_personal_area()
            main.wait_profile_text()
            assert main.profile_text_is_correct()

    @allure.title("Авторизация через ссылку в форме регистрации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_via_register_form_link(self, driver, new_user):
        main = MainPage(driver)
        auth = AuthPage(driver)
        register = RegisterPage(driver)
        with allure.step("Перейти к форме регистрации"):
            main.click_login_order_button()
            auth.click_register_link()
        with allure.step("Перейти обратно на страницу входа"):
            register.click_login_link()
        with allure.step("Авторизоваться"):
            main.login(new_user["email"], new_user["password"])
        with allure.step("Проверить профиль"):
            main.click_personal_area()
            main.wait_profile_text()
            assert main.profile_text_is_correct()

    @allure.title("Авторизация через ссылку в форме восстановления пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_via_forgot_password_form_link(self, driver, new_user):
        main = MainPage(driver)
        auth = AuthPage(driver)
        with allure.step("Перейти к форме восстановления пароля"):
            main.click_login_order_button()
            auth.click_forgot_password_link()
        with allure.step("Перейти обратно на страницу входа"):
            from locators.auth_locators import AuthLocators
            main.click(AuthLocators.LOGIN_LINK)
        with allure.step("Авторизоваться"):
            main.login(new_user["email"], new_user["password"])
        with allure.step("Проверить профиль"):
            main.click_personal_area()
            main.wait_profile_text()
            assert main.profile_text_is_correct()
