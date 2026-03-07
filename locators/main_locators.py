from selenium.webdriver.common.by import By


class MainLocators:
    PERSONAL_AREA_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_HEADER_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_HEADER_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGO = (By.XPATH, "//a[@href='/']")

    BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BURGER_CONST = (By.XPATH, "//span[@class='constructor-element__row']")
    LOGIN_ORDER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    BUN_TAB = (By.XPATH, "//span[text()='Булки']")
    BUN_TAB_SECTION = (By.XPATH, "//div[span[text()='Булки']]")
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")
    SAUCE_TAB_SECTION = (By.XPATH, "//div[span[text()='Соусы']]")
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")
    FILLING_TAB_SECTION = (By.XPATH, "//div[span[text()='Начинки']]")

    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@href,'/ingredient/')])[1]")
    INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@class,'BurgerIngredient')])[1]//p[contains(@class,'counter')]")

    INGREDIENT_POPUP = (By.XPATH, "//div[contains(@class,'Modal_modal__')]")
    INGREDIENT_POPUP_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//p[contains(@class,'Modal') and contains(text(),'идентификатор')]//following-sibling::h2 | //h2[contains(@class,'text_type_digits')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")