from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import (
    get_public_users_client,
)
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

user_to_create = CreateUserRequestSchema(
    email=get_random_email(),
    password="123123",
    first_name="artem",  # type: ignore
    last_name="aboba",  # type: ignore
    middle_name="jma",  # type: ignore
)

create_user_response = public_users_client.create_user(user_to_create)

authentication_user = AuthenticationUserSchema(
    email=user_to_create.email, password=user_to_create.password
)

files_client = get_files_client(authentication_user)

file_to_create = CreateFileRequestSchema(
    filename="negr.png", directory="negri", upload_file="testdata/files/negr.png"
)

courses_client = get_courses_client(authentication_user)

create_file_response = files_client.create_file(file_to_create)

course_to_create = CreateCourseRequestSchema(
    title="API",
    max_score=100,  # type: ignore
    min_score=10,  # type: ignore
    description="API Automation testing",
    estimated_time="2 week",  # type: ignore
    file_id=create_file_response.file.id,  # type: ignore
    created_by_user_id=create_user_response.user.id,  # type: ignore
)

print(courses_client.create_course(course_to_create))
