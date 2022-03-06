import requests

print(requests.delete("http://127.0.0.1:8080/api/users/1").json())