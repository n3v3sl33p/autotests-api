import httpx

BASE_URL = "http://127.0.0.1:8000/api/v1"
USER_CRED = {"email": "artem@mail.com", "password": "123123"}

with httpx.Client(base_url=BASE_URL) as client:
    login_response = client.post("/authentication/login", json=USER_CRED)
    access_token = login_response.json().get("token").get("accessToken")

    me_response = client.get(
        "/users/me", headers={"Authorization": f"Bearer {access_token}"}
    )

print("Satus code:", me_response.status_code)
print("Response:", me_response.json())
