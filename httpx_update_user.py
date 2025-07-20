import httpx

from tools.fakers import fake

BASE_URL = "http://127.0.0.1:8000/api/v1"

create_payload = {
    "email": fake.email(),
    "password": "123123",
    "lastName": "Aboba",
    "firstName": "Artem",
    "middleName": "JMA",
}

with httpx.Client(base_url=BASE_URL) as client:
    creaete_response = client.post("/users", json=create_payload)
    assert creaete_response.status_code == 200, "Ошибка создания пользователя"

    uid = creaete_response.json().get("user").get("id")

    login_response = client.post(
        "/authentication/login",
        json={
            "email": create_payload.get("email"),
            "password": create_payload.get("password"),
        },
    )
    assert login_response.status_code == 200, "Ошибка логина"

    access_token = login_response.json().get("token").get("accessToken")
    auth_header = {"Authorization": f"Bearer {access_token}"}
    client.headers.update(auth_header)

    update_payload = {
        "email": fake.email(),
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
    }

    update_response = client.patch(f"/users/{uid}", json=update_payload)
    print("Status code:", update_response.status_code)
    print("Response:", update_response.json())
