from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercise_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод для получения списка упражнений

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(
            "/api/v1/exercises", params=query.model_dump(by_alias=True)
        )

    def get_exercises(
        self, query: GetExercisesQuerySchema
    ) -> GetExercisesResponseSchema:
        """
        Метод для получения списка упражнений

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise_api(self, exerciseId: str) -> Response:
        """
        Метод для получения упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/exercises/{exerciseId}")

    def get_exercise(self, exerciseId: str) -> GetExerciseResponseSchema:
        """
        Метод для получения упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта GetExerciseResponseDict
        """
        response = self.get_exercise_api(exerciseId)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания упражнения
        :param request: Словарь CreateExerciseRequestDict
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post(
            "/api/v1/exercises", json=request.model_dump(by_alias=True)
        )

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        """
        Метод для создания упражнения
        :param request: Словарь CreateExerciseRequestDict
        :return: Ответ от сервера в виде объекта CreateExerciseResponseDict
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(
        self, id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод для обновления упражнения

        :param exerciseId: Id упражнения
        :param request: Словарь UpdateExerciseRuquestDict
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.patch(
            f"/api/v1/exercises/{id}", json=request.model_dump(by_alias=True)
        )

    def update_exercise(
        self, id: str, request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        """
        Метод для обновления упражнения

        :param exerciseId: Id упражнения
        :param request: Словарь UpdateExerciseRuquestDict
        :return: Ответ от сервера в виде объекта UpdateExerciseResponseDict
        """

        response = self.update_exercise_api(id, request)

        return UpdateExerciseResponseSchema.model_validate(response.text)

    def delete_exercise_api(self, exerciseId: str) -> Response:
        """
        Метод для удаления упражнения

        :param exerciseId: Id упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.delete(f"/api/v1/exercises{exerciseId}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
