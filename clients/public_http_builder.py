from httpx import Client

from config import settings


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """

    return Client(
        timeout=settings.http_client.timeout, base_url=settings.http_client.client_url
    )
