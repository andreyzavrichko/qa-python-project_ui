from selenium.webdriver.common.action_chains import ActionChains

from locators.auth_locators import AuthLocators
from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_personal_area(self):
        self.click(MainLocators.PERSONAL_AREA_BUTTON)

    def click_constructor_button(self):
        self.click(MainLocators.CONSTRUCTOR_HEADER_BUTTON)

    def click_order_feed_button(self):
        self.click(MainLocators.ORDER_FEED_HEADER_BUTTON)

    def click_logo(self):
        self.click(MainLocators.LOGO)

    def click_login_order_button(self):
        self.click(MainLocators.LOGIN_ORDER_BUTTON)

    def set_email(self, email: str):
        self.send_keys(AuthLocators.EMAIL_INPUT, email)

    def set_password(self, password: str):
        self.send_keys(AuthLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(AuthLocators.LOGIN_BUTTON)

    def login(self, email: str, password: str):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def click_bun_tab(self):
        self.click(MainLocators.BUN_TAB)

    def click_sauce_tab(self):
        self.click(MainLocators.SAUCE_TAB)

    def click_filling_tab(self):
        self.click(MainLocators.FILLING_TAB)

    def bun_tab_is_active(self) -> bool:
        cls = self.get_attribute(MainLocators.BUN_TAB_SECTION, "class")
        return "current" in cls

    def sauce_tab_is_active(self) -> bool:
        cls = self.get_attribute(MainLocators.SAUCE_TAB_SECTION, "class")
        return "current" in cls

    def filling_tab_is_active(self) -> bool:
        cls = self.get_attribute(MainLocators.FILLING_TAB_SECTION, "class")
        return "current" in cls

    def click_first_ingredient(self):
        self.click(MainLocators.FIRST_INGREDIENT)

    def ingredient_popup_is_visible(self) -> bool:
        return self.is_displayed(MainLocators.INGREDIENT_POPUP_TITLE)

    def close_popup(self):
        self.click(MainLocators.POPUP_CLOSE_BUTTON)

    def popup_is_closed(self) -> bool:
        self.wait_invisible(MainLocators.INGREDIENT_POPUP)
        return True

    def get_ingredient_counter(self) -> int:
        try:
            text = self.find(MainLocators.INGREDIENT_COUNTER).text
            return int(text) if text.isdigit() else 0
        except Exception:
            return 0

    def drag_ingredient_to_basket(self):
        ingredient = self.wait_visible(MainLocators.FIRST_INGREDIENT)
        target = self.wait_visible(MainLocators.BURGER_CONST)
        self._js_drag_and_drop(ingredient, target)

    # костыль для firefox
    def _js_drag_and_drop(self, source, target):
        self.driver.execute_script("""
            function simulateDragDrop(sourceNode, targetNode) {
                const EVENT_TYPES = ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'];
                function createEvent(type) {
                    const event = document.createEvent('DragEvent');
                    event.initMouseEvent(type, true, true, window, 0, 0, 0, 0, 0,
                        false, false, false, false, 0, null);
                    Object.defineProperty(event, 'dataTransfer', {
                        value: (() => {
                            let data = {};
                            return {
                                setData(k, v) { data[k] = v; },
                                getData(k) { return data[k]; },
                                clearData() { data = {}; },
                                setDragImage() {}
                            };
                        })()
                    });
                    return event;
                }
                sourceNode.dispatchEvent(createEvent('dragstart'));
                targetNode.dispatchEvent(createEvent('dragenter'));
                targetNode.dispatchEvent(createEvent('dragover'));
                targetNode.dispatchEvent(createEvent('drop'));
                sourceNode.dispatchEvent(createEvent('dragend'));
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """, source, target)

    def click_place_order(self):
        self.click(MainLocators.PLACE_ORDER_BUTTON)

    def get_order_number_from_modal(self) -> str:
        return self.get_text(MainLocators.ORDER_NUMBER_IN_MODAL)

    def wait_burger_title(self):
        self.wait_visible(MainLocators.BURGER_TITLE)

    def wait_profile_text(self):
        from locators.profile_locators import ProfileLocators
        self.wait_visible(ProfileLocators.PROFILE_INFO_TEXT)

    def profile_text_is_correct(self) -> bool:
        from locators.profile_locators import ProfileLocators
        text = self.get_text(ProfileLocators.PROFILE_INFO_TEXT)
        return "изменить свои персональные данные" in text
