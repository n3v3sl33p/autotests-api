from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient, GetCoursesQuerySchema
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from fixtures.courses import CourseFixture, UserFixture
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_create_course_response,
    assert_get_courses_response,
    assert_update_course_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(
        self, courses_client: CoursesClient, function_course: CourseFixture
    ):
        # Формируем данные для обновления
        request = UpdateCourseRequestSchema()
        # Отправляем запрос на обновление курса
        response = courses_client.update_course_api(
            function_course.response.course.id, request
        )
        # Преобразуем JSON-ответ в объект схемы
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные в ответе соответствуют запросу
        assert_update_course_response(request, response_data)

        # Валидируем JSON-схему ответа
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_courses(
        self,
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_course: CourseFixture,
    ):
        # Формируем параметры запроса, передавая user_id
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)  # type: ignore
        # Отправляем GET-запрос на получение списка курсов
        response = courses_client.get_courses_api(query)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список курсов соответствует ранее созданным курсам
        assert_get_courses_response(response_data, [function_course.response])

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_course(
        self,
        courses_client: CoursesClient,
        function_file: FileFixture,
        function_user: UserFixture,
    ):
        request = CreateCourseRequestSchema(
            previewFileId=function_file.response.file.id,
            createdByUserId=function_user.response.user.id,
        )
        response = courses_client.create_course_api(request)

        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
