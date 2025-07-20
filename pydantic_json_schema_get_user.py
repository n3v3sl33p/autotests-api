from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_payload = CreateUserRequestSchema(
    email=fake.email(),
    password="123",
    first_name="artem",  # type: ignore
    last_name="aboba",  # type: ignore
    middle_name="jma",  # type: ignore
)
create_user_response = public_users_client.create_user(create_user_payload)

user = AuthenticationUserSchema(
    email=create_user_payload.email, password=create_user_payload.password
)

private_users_client = get_private_users_client(user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(get_user_response.json(), get_user_response_schema)
