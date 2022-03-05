import requests
from requests import post, delete

print(requests.get("http://127.0.0.1:8080/api/jobs").json())
print(requests.get("http://127.0.0.1:8080/api/jobs/2").json())
print(requests.get("http://127.0.0.1:8080/api/jobs/777").json())
print(requests.get("http://127.0.0.1:8080/api/jobs/erew").json())


print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1,
                 'id': 6,
                 'job': 'adding new tests',
                 'work_size': 11,
                 'collaborators': '2, 5',
                 'is_finished': False}).json())