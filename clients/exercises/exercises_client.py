from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.builders.private_http_builder import (
    AuthenticationUserDict,
    get_private_http_client,
)


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнений
    """

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание стрктуры запроса для создания упражнения
    """

    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроа для обновления упражнения
    """

    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class Exercise(TypedDict):
    """
    Модель упражнения
    """

    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа от сервера для создания упражнения
    """

    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа от сервера для получения упражнения
    """

    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа от сервера для получения упражнений
    """

    exercises: list[Exercise]


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа от сервера для обновления упражнения
    """

    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(
            "/api/v1/exercises", params={"courseId": query.get("courseId")}
        )

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод для получения списка упражнений

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта GetExercisesResponseDict
        """
        return self.get_exercises_api(query).json()

    def get_exercise_api(self, exerciseId: str) -> Response:
        """
        Метод для получения упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/exercises/{exerciseId}")

    def get_exercise(self, exerciseId: str) -> GetExerciseResponseDict:
        """
        Метод для получения упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта GetExerciseResponseDict
        """
        return self.get_exercise_api(exerciseId).json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения
        :param request: Словарь CreateExerciseRequestDict
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/exercises", json=request)

    def create_exercise(
        self, request: CreateExerciseRequestDict
    ) -> CreateExerciseResponseDict:
        """
        Метод для создания упражнения
        :param request: Словарь CreateExerciseRequestDict
        :return: Ответ от сервера в виде объекта CreateExerciseResponseDict
        """
        return self.create_exercise_api(request).json()

    def update_exercise_api(
        self, exerciseId: str, request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод для обновления упражнения

        :param exerciseId: Id упражнения
        :param request: Словарь UpdateExerciseRuquestDict
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.patch(f"/api/v1/exercises{exerciseId}", json=request)

    def update_exercise(
        self, exerciseId: str, request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        """
        Метод для обновления упражнения

        :param exerciseId: Id упражнения
        :param request: Словарь UpdateExerciseRuquestDict
        :return: Ответ от сервера в виде объекта UpdateExerciseResponseDict
        """
        return self.update_exercise_api(exerciseId, request).json()

    def delete_exercise_api(self, exerciseId: str) -> Response:
        """
        Метод для удаления упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.delete(f"/api/v1/exercises{exerciseId}")


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
