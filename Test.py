import requests
print(requests.get("http://localhost:8080/API/Password-Generator").json()["generated password"])