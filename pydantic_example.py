from typing import Any

from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")


user_data: dict[str, Any] = {
    "id": 222,
    "name": "artem",
    "email": "artem@mail.com",
    "isActive": True,
}
user = User(**user_data)
print(user)


# user = User(
#     id=1,
#     name="Alice",
#     email="alice@mail.com",
# )

# print(user.model_dump())
