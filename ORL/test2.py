from requests import get, post, delete


print(get('http://localhost:8080/api/v2/jobs').json())
print(get('http://localhost:8080/api/v2/jobs/2').json())
print(get('http://localhost:8080/api/v2/jobs/999').json())
print(get('http://localhost:8080/api/v2/jobs/q').json())
print(post('http://localhost:8080/api/v2/jobs').json())
print(post('http://localhost:8080/api/v2/jobs', json={'team_leader': 1}).json())
print(post('http://localhost:8080/api/v2/jobs', json={
    'team_leader': 1,
    'job': 'yandex lyceum lesson',
    'work_size': 10,
    'collaborators': '3, 4',
    'is_finished': 1}).json())
print(delete('http://localhost:8080/api/v2/jobs/999').json()) # работ с id = 999 нет в базе
print(delete('http://localhost:8080/api/v2/jobs/12').json())