from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.builders.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры пользователя.
    """

    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа на создание создание пользователя
    """

    user: User


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.

    Attributes:
        email (str): Электронная почта пользователя.
        password (str): Пароль пользователя.
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создаёт нового пользователя через публичный API.

        Args:
            request (CreateUserRequestDict): Словарь с данными нового пользователя. Должен содержать email, пароль, фамилию, имя и отчество.

        Returns:
            Response: Объект ответа от сервера, содержащий статус и тело ответа.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
