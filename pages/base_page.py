from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WAIT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.wait_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            # костыль для firefox
            self._wait_overlay_gone()
            self.wait_clickable(locator).click()

    def _wait_overlay_gone(self, timeout: int = 15):
        from selenium.webdriver.common.by import By
        overlay_locator = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")
        end = __import__("time").time() + timeout
        # Сначала ждём появления (на случай если ещё не рендерился)
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(overlay_locator)
            )
        except Exception:
            pass  # оверлей уже ушёл или не появится — ok
        # Затем ждём исчезновения
        WebDriverWait(self.driver, max(1, end - __import__("time").time())).until(
            EC.invisibility_of_element_located(overlay_locator)
        )

    def send_keys(self, locator, text: str):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    def wait_visible(self, locator, timeout: int = WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: int = WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_invisible(self, locator, timeout: int = WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def get_attribute(self, locator, attribute: str) -> str:
        return self.wait_visible(locator).get_attribute(attribute)
