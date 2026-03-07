import uuid

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager


from config import BASE_URL
from helpers.api_client import ApiClient

fake = Faker()
# костыль при исчерпании лимитов скачивания
GECKO_DRIVER_PATH = r"C:\Users\a.zavrichko\.wdm\drivers\geckodriver\win64\v0.36.0\geckodriver.exe"


@pytest.fixture(params=["chrome", "firefox"], ids=["chrome", "firefox"])
def driver(request):
    """Кроссбраузерная фикстура. Запускает тест в Chrome и Firefox."""
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(GECKO_DRIVER_PATH)
        web_driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")

    web_driver.set_window_size(1920, 1080)
    web_driver.get(BASE_URL)

    yield web_driver

    web_driver.quit()


@pytest.fixture
def new_user():
    unique = uuid.uuid4().hex[:8]
    user_data = ApiClient.create_user(
        name=fake.first_name(),
        email=f"test_{unique}@test.com",
        password=fake.password(length=8),
    )
    yield user_data
    ApiClient.delete_user(user_data["access_token"])


@pytest.fixture
def authenticated_driver(driver, new_user):
    driver.get(BASE_URL)
    driver.execute_script(
        """
        localStorage.setItem('accessToken', arguments[0]);
        localStorage.setItem('refreshToken', arguments[1]);
        """,
        new_user["access_token"],
        new_user["refresh_token"],
    )
    driver.refresh()
    yield driver, new_user
