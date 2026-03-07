import allure
from faker import Faker
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.register_page import RegisterPage
from helpers.api_client import ApiClient

fake = Faker()


@allure.feature("Регистрация")
class TestRegister:

    @allure.title("Успешная регистрация нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(self, driver):
        main = MainPage(driver)
        auth = AuthPage(driver)
        register = RegisterPage(driver)

        email = fake.email()
        password = fake.password(length=8)
        name = fake.first_name()

        with allure.step("Перейти на страницу регистрации"):
            main.click_personal_area()
            auth.click_register_link()
        with allure.step("Заполнить форму регистрации"):
            register.set_name(name)
            register.set_email(email)
            register.set_password(password)
            register.click_register_button()
        with allure.step("Проверить редирект на страницу входа"):
            auth.wait_auth_page()
            assert auth.auth_title_text() == "Вход"

        tokens = ApiClient.login_user(email, password)
        ApiClient.delete_user(tokens["access_token"])

    @allure.title("Регистрация с паролем менее 6 символов — ошибка")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration_with_short_password_shows_error(self, driver):
        main = MainPage(driver)
        auth = AuthPage(driver)
        register = RegisterPage(driver)

        with allure.step("Перейти на страницу регистрации"):
            main.click_personal_area()
            auth.click_register_link()
        with allure.step("Заполнить форму с паролем из 1 символа"):
            register.set_name(fake.first_name())
            register.set_email(fake.email())
            register.set_password("1")
            register.click_register_button()
        with allure.step("Проверить отображение ошибки"):
            assert register.incorrect_password_error_text() == "Некорректный пароль"