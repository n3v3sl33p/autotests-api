from pydantic import BaseModel, EmailStr, Field

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """

    token: TokenSchema


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.uuid4)
