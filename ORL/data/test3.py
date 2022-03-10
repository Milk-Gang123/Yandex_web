import requests
from requests import post, delete


print(requests.get("http://127.0.0.1:8080/api/jobs").json())

# Удаление 5-й записи (верный)
print(delete('http://localhost:8080/api/jobs/5').json())

# Удаление несуществующей 555-й записи (неверный)
print(delete('http://localhost:8080/api/jobs/555').json())

# Удаление записи в виде строки (неверный)
print(delete('http://localhost:8080/api/jobs/aboba').json())

# Повторный вывод (верный)
print(requests.get("http://127.0.0.1:8080/api/jobs").json())

# Вывод программы
''' {'news': [{'collaborators': '4, 5', 'end_date': '2022-03-02 22:21:47', 'id': 2, 'is_finished': False, 'job': 'repair my brain', 'start_date': '2022-03-02 22:21:47', 'team_leader': 1, 'work_size': 9999}, {'collaborators': '3, 6', 'end_date': '2022-03-02 22:26:16', 'id': 3, 'is_finished': True, 'job': 'Hard workout', 'start_date': '2022-03-02 22:26:16', 'team_leader': 1, 'work_size': 5}, {'collaborators': '2, 3', 'end_date': '2022-03-03 22:10:50', 'id': 4, 'is_finished': False, 'job': 'repair module 1 and 2', 'start_date': '2022-03-03 22:10:50', 'team_leader': 1, 'work_size': 15}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:57:36', 'id': 5, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:57:36', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:58:09', 'id': 6, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:58:09', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:59:36', 'id': 7, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:59:36', 'team_leader': 1, 'work_size': 11}]}
    {'success': 'OK'}
    {'error': 'Not found'}
    {'error': 'Not found'}
    {'news': [{'collaborators': '4, 5', 'end_date': '2022-03-02 22:21:47', 'id': 2, 'is_finished': False, 'job': 'repair my brain', 'start_date': '2022-03-02 22:21:47', 'team_leader': 1, 'work_size': 9999}, {'collaborators': '3, 6', 'end_date': '2022-03-02 22:26:16', 'id': 3, 'is_finished': True, 'job': 'Hard workout', 'start_date': '2022-03-02 22:26:16', 'team_leader': 1, 'work_size': 5}, {'collaborators': '2, 3', 'end_date': '2022-03-03 22:10:50', 'id': 4, 'is_finished': False, 'job': 'repair module 1 and 2', 'start_date': '2022-03-03 22:10:50', 'team_leader': 1, 'work_size': 15}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:58:09', 'id': 6, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:58:09', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:59:36', 'id': 7, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:59:36', 'team_leader': 1, 'work_size': 11}]}'''