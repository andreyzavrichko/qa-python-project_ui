from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following::input[1]")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_INPUT_CONTAINER = (
        By.XPATH,
        "//input[@name='Введите новый пароль']/parent::div"
    )
