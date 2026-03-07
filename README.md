# Stellar Burgers — UI Autotests

Автотесты для веб-приложения [Stellar Burgers](https://stellarburgers.education-services.ru/).  
Стек: Python 3.12+, Selenium, pytest, Allure, Requests.

---

## Структура проекта

```
stellar_burgers/
├── config.py                   # BASE_URL и API_URL
├── conftest.py                 # фикстуры: driver, new_user, authenticated_driver
├── pytest.ini                  # настройки pytest + allure-results dir
├── requirements.txt
├── helpers/
│   └── api_client.py           # создание/удаление пользователей и заказов через API
├── locators/                   # By-локаторы, сгруппированные по страницам
├── pages/                      # Page Object Model
│   ├── base_page.py            # общие методы (click, send_keys, wait_visible …)
│   └── *.py                    # страница — отдельный класс
└── tests/
    ├── test_auth.py            # 4 теста — авторизация
    ├── test_register.py        # 2 теста — регистрация
    ├── test_profile.py         # 5 тестов — личный кабинет
    ├── test_main.py            # 8 тестов — конструктор / ингредиенты
    ├── test_forgot_password.py # 3 теста — восстановление пароля
    └── test_order_feed.py      # 5 тестов — лента заказов
```

---

## Установка

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Chrome и Firefox должны быть установлены — драйверы скачиваются автоматически через `webdriver-manager`.

---

## Запуск

```bash
# Все тесты в Chrome и Firefox
pytest tests/

# Только Chrome
pytest tests/ --browser=chrome

# Один тест-файл
pytest tests/test_auth.py -v

# С выводом в консоль
pytest tests/ -v -s
```

---

## Allure-отчёт

```bash
# Запустить тесты и сгенерировать отчёт
pytest tests/
allure serve allure-results
```

---

## Ключевые решения

| Решение | Причина |
|---|---|
| Пользователи создаются через API (`ApiClient`) | Тесты независимы; нет хардкода учётных данных |
| `authenticated_driver` инжектирует токены в `localStorage` | Избегаем UI-логина в каждом тесте |
| Фикстура `driver` параметризована `[chrome, firefox]` | Каждый тест автоматически прогоняется в двух браузерах |
| Локаторы вынесены в отдельный пакет `locators/` | Локатор меняется в одном месте |
| `BasePage` содержит все ожидания | Нет прямых вызовов `WebDriverWait` в Page Object и тестах |