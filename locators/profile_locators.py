from selenium.webdriver.common.by import By


class ProfileLocators:
    PROFILE_INFO_TEXT = (By.XPATH, "//nav[contains(@class,'Account_nav')]//p[1]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    ORDER_HISTORY_TITLE = (By.XPATH, "//h2[text()='История заказов']")
    ORDER_HISTORY_ITEM = (
        By.XPATH,
        "//li[contains(@class,'OrderHistory_listItem')]"
    )