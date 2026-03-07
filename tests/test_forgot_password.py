import allure
from faker import Faker
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.forgot_password_page import ForgotPasswordPage

fake = Faker()


@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_forgot_password_page(self, driver):
        main = MainPage(driver)
        auth = AuthPage(driver)
        forgot = ForgotPasswordPage(driver)
        with allure.step("Перейти на страницу входа"):
            main.click_personal_area()
        with allure.step("Кликнуть «Восстановить пароль»"):
            auth.click_forgot_password_link()
        with allure.step("Проверить открытие страницы восстановления пароля"):
            forgot.wait_forgot_password_page()
            assert forgot.forgot_password_title_is_visible()

    @allure.title("Ввод email и клик «Восстановить» переводит на страницу сброса пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enter_email_and_click_restore(self, driver):
        main = MainPage(driver)
        auth = AuthPage(driver)
        forgot = ForgotPasswordPage(driver)
        with allure.step("Перейти на страницу восстановления"):
            main.click_personal_area()
            auth.click_forgot_password_link()
            forgot.wait_forgot_password_page()
        with allure.step("Ввести email и нажать «Восстановить»"):
            forgot.set_email(fake.email())
            forgot.click_restore_button()
        with allure.step("Проверить переход на /reset-password"):
            assert forgot.reset_password_page_is_open()

    @allure.title("Клик по иконке показать/скрыть пароль делает поле активным")
    @allure.severity(allure.severity_level.NORMAL)
    def test_show_hide_password_activates_input(self, driver):
        main = MainPage(driver)
        auth = AuthPage(driver)
        forgot = ForgotPasswordPage(driver)
        with allure.step("Перейти на страницу восстановления и запросить сброс"):
            main.click_personal_area()
            auth.click_forgot_password_link()
            forgot.wait_forgot_password_page()
            forgot.set_email(fake.email())
            forgot.click_restore_button()
        with allure.step("Кликнуть на иконку показать/скрыть пароль"):
            forgot.click_show_hide_password()
        with allure.step("Проверить, что поле пароля стало активным"):
            assert forgot.password_input_is_active()
