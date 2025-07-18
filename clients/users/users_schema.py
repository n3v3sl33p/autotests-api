from pydantic import BaseModel, ConfigDict, EmailStr, Field

from clients.private_http_builder import AuthenticationUserSchema


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    user: UserSchema


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """

    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """

    user: UserSchema


class CreateUserRequestSchema(AuthenticationUserSchema):
    """
    Описание структуры запроса на создание пользователя.
    """

    model_config = ConfigDict(populate_by_name=True)

    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
