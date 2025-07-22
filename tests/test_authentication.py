from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
)
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(
    authentication_client: AuthenticationClient,
    function_user: UserFixture,
):
    request = LoginRequestSchema(
        email=function_user.email, password=function_user.password
    )
    response = authentication_client.login_api(request)
    assert_status_code(response.status_code, HTTPStatus.OK)

    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_login_response(response_data)
    validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())
