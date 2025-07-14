import httpx


# получаем token
data = {
  "email": "kirill@mail.com",
  "password": "123123"
}

response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=data)

access_token = response.json()["token"]["accessToken"]


# отправляем запрос на /users/me с токеном
headers = {"Authorization": f"Bearer {access_token}"}

response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)

print(response.status_code, response.json(), sep='\n')