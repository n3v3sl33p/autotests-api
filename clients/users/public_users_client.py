from typing import TypedDict

from httpx import Client, Response

from clients.api_client import APIClient


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
