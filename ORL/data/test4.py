import requests
from requests import post, delete, put

print(put('http://localhost:8080/api/jobs/7',
           json={'is_finished': True}).json())