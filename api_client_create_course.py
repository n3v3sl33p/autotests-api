from clients.builders.private_http_builder import AuthenticationUserDict
from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.users.public_users_client import (
    CreateUserRequestDict,
    get_public_users_client,
)
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

user_to_create = CreateUserRequestDict(
    email=get_random_email(),
    password="123123",
    firstName="artem",
    lastName="aboba",
    middleName="jma",
)

create_user_response = public_users_client.create_user(user_to_create)

authentication_user = AuthenticationUserDict(
    email=user_to_create.get("email"), password=user_to_create.get("password")
)

files_client = get_files_client(authentication_user)

file_to_create = CreateFileRequestDict(
    filename="negr.png", directory="negri", upload_file="testdata/files/negr.png"
)

courses_client = get_courses_client(authentication_user)

create_file_response = files_client.create_file(file_to_create)

course_to_create = CreateCourseRequestDict(
    title="API",
    maxScore=100,
    minScore=10,
    description="API Automation testing",
    estimatedTime="2 week",
    previewFileId=create_file_response.get("file").get("id"),
    createdByUserId=create_user_response.get("user").get("id"),
)

print(courses_client.create_course(course_to_create))
