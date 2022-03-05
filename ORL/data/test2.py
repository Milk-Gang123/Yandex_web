import requests
from requests import post, delete

print(requests.get("http://127.0.0.1:8080/api/jobs").json())

# корректный запрос (верный)
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1,
                 'job': 'adding new tests',
                 'work_size': 11,
                 'collaborators': '2, 5',
                 'is_finished': False}).json())

# пустой запрос (неверный)
print(post('http://localhost:8080/api/jobs').json())

# запрос, в котором недостаточно данных (неверный)
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1,
                 'job': 'adding new tests'}).json())

# запрос с существующим id (неверный)
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1,
                 'id': 2,
                 'job': 'adding new tests',
                 'work_size': 11,
                 'collaborators': '2, 5',
                 'is_finished': False}).json())


print(requests.get("http://127.0.0.1:8080/api/jobs").json())

#ывод программы
''' {'news': [{'collaborators': '4, 5', 'end_date': '2022-03-02 22:21:47', 'id': 2, 'is_finished': False, 'job': 'repair my brain', 'start_date': '2022-03-02 22:21:47', 'team_leader': 1, 'work_size': 9999}, {'collaborators': '3, 6', 'end_date': '2022-03-02 22:26:16', 'id': 3, 'is_finished': True, 'job': 'Hard workout', 'start_date': '2022-03-02 22:26:16', 'team_leader': 1, 'work_size': 5}, {'collaborators': '2, 3', 'end_date': '2022-03-03 22:10:50', 'id': 4, 'is_finished': False, 'job': 'repair module 1 and 2', 'start_date': '2022-03-03 22:10:50', 'team_leader': 1, 'work_size': 15}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:57:36', 'id': 5, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:57:36', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:58:09', 'id': 6, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:58:09', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:59:36', 'id': 7, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:59:36', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 20:00:22', 'id': 8, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 20:00:22', 'team_leader': 1, 'work_size': 11}]}
    {'success': 'OK'}
    {'error': 'Empty request'}
    {'error': 'Bad request'}
    {'error': 'Id already exists'}
    {'news': [{'collaborators': '4, 5', 'end_date': '2022-03-02 22:21:47', 'id': 2, 'is_finished': False, 'job': 'repair my brain', 'start_date': '2022-03-02 22:21:47', 'team_leader': 1, 'work_size': 9999}, {'collaborators': '3, 6', 'end_date': '2022-03-02 22:26:16', 'id': 3, 'is_finished': True, 'job': 'Hard workout', 'start_date': '2022-03-02 22:26:16', 'team_leader': 1, 'work_size': 5}, {'collaborators': '2, 3', 'end_date': '2022-03-03 22:10:50', 'id': 4, 'is_finished': False, 'job': 'repair module 1 and 2', 'start_date': '2022-03-03 22:10:50', 'team_leader': 1, 'work_size': 15}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:57:36', 'id': 5, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:57:36', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:58:09', 'id': 6, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:58:09', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:59:36', 'id': 7, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:59:36', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 20:00:22', 'id': 8, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 20:00:22', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 20:17:28', 'id': 9, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 20:17:28', 'team_leader': 1, 'work_size': 11}]}
    '''