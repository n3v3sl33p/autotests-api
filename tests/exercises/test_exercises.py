from http import HTTPStatus

import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercise_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from clients.exercises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_exercise_not_found_response,
    assert_get_exercise_response,
    assert_get_exercises_response,
    assert_update_exercise_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    def test_create_exercises(
        self, exercises_client: ExercisesClient, function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(courseId=function_course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()

        response = exercises_client.update_exercise_api(
            id=function_exercise.id, request=request
        )

        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        response_delete = exercises_client.delete_exercise_api(function_exercise.id)

        assert_status_code(response_delete.status_code, HTTPStatus.OK)

        response_get = exercises_client.get_exercise_api(function_exercise.id)

        assert_status_code(response_get.status_code, HTTPStatus.NOT_FOUND)
        response_data = InternalErrorResponseSchema.model_validate_json(
            response_get.text
        )
        assert_exercise_not_found_response(response_data)

        validate_json_schema(response_get.json(), response_data.model_json_schema())

    def test_get_exercises(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        query = GetExercisesQuerySchema(
            courseId=function_exercise.response.exercise.course_id
        )
        response = exercises_client.get_exercises_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        print("JSON", response.json())

        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
