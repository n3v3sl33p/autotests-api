from clients.users import public_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# print(TokenSchema.model_json_schema())
"""
{
    "description": "Описание структуры аутентификационных токенов.",
    "properties": {
        "tokenType": {"title": "Tokentype", "type": "string"},
        "accessToken": {"title": "Accesstoken", "type": "string"},
        "refreshToken": {"title": "Refreshtoken", "type": "string"},
    },
    "required": ["tokenType", "accessToken", "refreshToken"],
    "title": "TokenSchema",
    "type": "object",
}
"""
public_users_client = get_public_users_client()

create_user_payload = CreateUserRequestSchema(
    email=get_random_email(),
    password="123",
    first_name="artem",  # type: ignore
    last_name="aboba",  # type: ignore
    middle_name="jma",  # type: ignore
)

create_user_response = public_users_client.create_user_api(create_user_payload)
create_user_response_json = create_user_response.json()

create_user_response_schema = CreateUserResponseSchema.model_json_schema()
validate_json_schema(create_user_response_json, create_user_response_schema)

"""
{
  "type": "object",
  "properties": {
    "username": {"type": "string", "minLength": 5, "maxLength": 15}
  },
  "required": ["username"]
}

"""
