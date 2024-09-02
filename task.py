import requests

response = requests.post(
    "http://localhost:5000/login",
    json={"username": "user", "password": "password"},
)
token = response.json()["token"]
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("http://localhost:5000/private", headers = headers)
print(response.json())