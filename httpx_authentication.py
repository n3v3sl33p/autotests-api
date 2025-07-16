import httpx

login_payload = {"email": "artem@mail.com", "password": "123123"}


BASE_URL = "http://127.0.0.1:8000/api/v1/authentication"

login_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload
)


login_response_data = login_response.json()

print("login response:", login_response_data)
print("status code:", login_response.status_code)

refresh_payload = {"refreshToken": login_response_data.get("token").get("refreshToken")}

refresh_response = httpx.post(f"{BASE_URL}/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh response:", refresh_response_data)
print("Refresh status code:", refresh_response.status_code)
