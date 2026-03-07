import requests
from config import API_URL


class ApiClient:
    @staticmethod
    def create_user(name: str, email: str, password: str) -> dict:
        """Создать пользователя через API. Вернуть {email, password, token}."""
        response = requests.post(
            f"{API_URL}/auth/register",
            json={"name": name, "email": email, "password": password},
        )
        assert response.status_code == 200, (
            f"Не удалось создать пользователя: {response.text}"
        )
        body = response.json()
        return {
            "name": name,
            "email": email,
            "password": password,
            "access_token": body["accessToken"],
            "refresh_token": body["refreshToken"],
        }

    @staticmethod
    def delete_user(access_token: str) -> None:
        """Удалить пользователя через API."""
        response = requests.delete(
            f"{API_URL}/auth/user",
            headers={"Authorization": access_token},
        )
        assert response.status_code == 202, (
            f"Не удалось удалить пользователя: {response.text}"
        )

    @staticmethod
    def login_user(email: str, password: str) -> dict:
        """Авторизовать пользователя. Вернуть токены."""
        response = requests.post(
            f"{API_URL}/auth/login",
            json={"email": email, "password": password},
        )
        assert response.status_code == 200, (
            f"Не удалось авторизоваться: {response.text}"
        )
        body = response.json()
        return {
            "access_token": body["accessToken"],
            "refresh_token": body["refreshToken"],
        }

    @staticmethod
    def get_ingredients() -> list:
        """Получить список ингредиентов."""
        response = requests.get(f"{API_URL}/ingredients")
        assert response.status_code == 200
        return response.json()["data"]

    @staticmethod
    def create_order(access_token: str, ingredient_ids: list) -> dict:
        """Создать заказ через API."""
        response = requests.post(
            f"{API_URL}/orders",
            json={"ingredients": ingredient_ids},
            headers={"Authorization": access_token},
        )
        assert response.status_code == 200, (
            f"Не удалось создать заказ: {response.text}"
        )
        return response.json()

    @staticmethod
    def get_user_orders(access_token: str) -> list:
        """Получить заказы пользователя."""
        response = requests.get(
            f"{API_URL}/orders",
            headers={"Authorization": access_token},
        )
        assert response.status_code == 200
        return response.json()["orders"]
