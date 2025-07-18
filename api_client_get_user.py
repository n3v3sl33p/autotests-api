# from clients.courses.courses_client import CreateCourseRequestDict
from clients.builders.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import (
    CreateUserRequestDict,
    get_public_users_client,
)
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="test",
    firstName="test",
    lastName="test",
    middleName="test",
)

create_user_response = public_users_client.create_user(create_user_request)


print("Create user response data: ", create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"],
)

private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user(
    create_user_response.get("user").get("id")
)


print("Get user response data: ", get_user_response)
