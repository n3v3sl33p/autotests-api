from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнений
    """

    courseId: str


class CreateExereciseRequestDict(TypedDict):
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
        return self.client.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exerciseId: str) -> Response:
        """
        Метод для получения упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/exercises/{exerciseId}")

    def create_exercise_api(self, request: CreateExereciseRequestDict) -> Response:
        """
        Метод для создания упражнения
        :param request: Словарь CreateExerciseRequestDict
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/exercises", json=request)

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

    def delete_exercise_api(self, exerciseId: str) -> Response:
        """
        Метод для удаления упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.delete(f"/api/v1/exercises{exerciseId}")
