from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import (
    get_public_users_client,
)
from clients.users.users_schema import CreateUserRequestSchema

public_users_client = get_public_users_client()

user_to_create = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(user_to_create)

authentication_user = AuthenticationUserSchema(
    email=user_to_create.email, password=user_to_create.password
)

files_client = get_files_client(authentication_user)

file_to_create = CreateFileRequestSchema(upload_file="testdata/files/negr.png")

courses_client = get_courses_client(authentication_user)

create_file_response = files_client.create_file(file_to_create)

course_to_create = CreateCourseRequestSchema(
    file_id=create_file_response.file.id,  # type: ignore
    created_by_user_id=create_user_response.user.id,  # type: ignore
)

print(courses_client.create_course(course_to_create))
