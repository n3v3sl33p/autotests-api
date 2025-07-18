from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.builders.private_http_builder import (
    AuthenticationUserDict,
    get_private_http_client,
)
from clients.files.files_client import File
from clients.users.public_users_client import User


class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """

    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """

    userId: str


class UpadateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """

    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class Course(TypedDict):
    """
    Описание структуры курса.
    """

    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """

    course: Course


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(
            "/api/v1/courses", params={"userId": query.get("userId")}
        )

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/courses", json=request)

    def create_course(
        self, request: CreateCourseRequestDict
    ) -> CreateCourseResponseDict:
        return self.create_course_api(request).json()

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/courses/{course_id}")

    def update_course_api(
        self, course_id: str, request: UpadateCourseRequestDict
    ) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.delete(f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
