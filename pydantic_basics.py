"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""

from typing import Any

from pydantic import BaseModel, Field


class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimatedTime: str = Field(alias="estimatedTime")


class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


course_default_model = CourseSchema(
    id="Course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright description",
    estimatedTime="2 week",
)
print(course_default_model)

course_dict: dict[str, Any] = {
    "id": "Course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright description",
    "estimatedTime": "2 week",
}

model_from_dict = CourseSchema(**course_dict)
print(model_from_dict)

course_json = """
{
    "id": "string",
    "title": "string",
    "maxScore": 100,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "2 week"
}
"""

model_from_json = CourseSchema.model_validate_json(course_json)
print(model_from_json)
print(model_from_json.model_dump_json(by_alias=True))
