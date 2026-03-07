from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_ORDER_ITEM = (By.XPATH, "(//ul[contains(@class,'OrderFeed')]//li | //div[contains(@class,'Feed_feed')]//li)[1]")
    ORDER_ITEM_NUMBER = (By.XPATH, "//p[contains(@class,'text_type_digits-default')]")

    ORDER_DETAILS_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")

    DONE_ALL_TIME_COUNTER = (By.XPATH, "(//p[contains(@class,'OrderFeed_number__')])[1] | //p[contains(text(),'Выполнено за всё время')]/following-sibling::p")
    DONE_TODAY_COUNTER = (By.XPATH, "(//p[contains(@class,'OrderFeed_number__')])[2] | //p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")

    IN_PROGRESS_ORDER_NUMBER = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderListReady')]//li[contains(@class,'text_type_digits-default')]"
    )