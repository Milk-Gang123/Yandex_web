import requests
from requests import post, delete, put


print(requests.get("http://127.0.0.1:8080/api/jobs").json())

# Изменение 4-й записи (верный)
print(put('http://localhost:8080/api/jobs/4', json={'work_size': 35}).json())

# Изменение несуществующей 555-й записи (неверный)
print(put('http://localhost:8080/api/jobs/555').json())

# Изменение записи в виде строки (неверный)
print(put('http://localhost:8080/api/jobs/aboba', json={'work_size': 35}).json())

# Пустой запрос (неверный)
print(put('http://localhost:8080/api/jobs/5').json())

# Повторный вывод (верный)
print(requests.get("http://127.0.0.1:8080/api/jobs").json())

# Вывод программы
''' {'news': [{'collaborators': '4, 5', 'end_date': '2022-03-02 22:21:47', 'id': 2, 'is_finished': False, 'job': 'repair my brain', 'start_date': '2022-03-02 22:21:47', 'team_leader': 1, 'work_size': 9999}, {'collaborators': '3, 6', 'end_date': '2022-03-02 22:26:16', 'id': 3, 'is_finished': True, 'job': 'Hard workout', 'start_date': '2022-03-02 22:26:16', 'team_leader': 1, 'work_size': 5}, {'collaborators': '2, 3', 'end_date': '2022-03-03 22:10:50', 'id': 4, 'is_finished': False, 'job': 'repair module 1 and 2', 'start_date': '2022-03-03 22:10:50', 'team_leader': 1, 'work_size': 15}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:58:09', 'id': 6, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:58:09', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:59:36', 'id': 7, 'is_finished': True, 'job': 'adding new tests 2 35', 'start_date': '2022-03-05 19:59:36', 'team_leader': 1, 'work_size': 20}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:45:26', 'id': 8, 'is_finished': False, 'job': 'adding new tests 2', 'start_date': '2022-03-05 21:45:26', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:45:48', 'id': 9, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 21:45:48', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:47:47', 'id': 10, 'is_finished': False, 'job': 'adding new tests 2 3 4', 'start_date': '2022-03-05 21:47:47', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:48:01', 'id': 11, 'is_finished': False, 'job': 'adding new tests 2 3 4', 'start_date': '2022-03-05 21:48:01', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:48:42', 'id': 12, 'is_finished': False, 'job': 'adding new tests 2 3 4', 'start_date': '2022-03-05 21:48:42', 'team_leader': 1, 'work_size': 11}]}
    {'success': 'OK'}
    {'error': 'Empty request'}
    {'error': 'Not found'}
    {'error': 'Empty request'}
    {'news': [{'collaborators': '4, 5', 'end_date': '2022-03-02 22:21:47', 'id': 2, 'is_finished': False, 'job': 'repair my brain', 'start_date': '2022-03-02 22:21:47', 'team_leader': 1, 'work_size': 9999}, {'collaborators': '3, 6', 'end_date': '2022-03-02 22:26:16', 'id': 3, 'is_finished': True, 'job': 'Hard workout', 'start_date': '2022-03-02 22:26:16', 'team_leader': 1, 'work_size': 5}, {'collaborators': '2, 3', 'end_date': '2022-03-03 22:10:50', 'id': 4, 'is_finished': False, 'job': 'repair module 1 and 2', 'start_date': '2022-03-03 22:10:50', 'team_leader': 1, 'work_size': 35}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:58:09', 'id': 6, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 19:58:09', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 19:59:36', 'id': 7, 'is_finished': True, 'job': 'adding new tests 2 35', 'start_date': '2022-03-05 19:59:36', 'team_leader': 1, 'work_size': 20}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:45:26', 'id': 8, 'is_finished': False, 'job': 'adding new tests 2', 'start_date': '2022-03-05 21:45:26', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:45:48', 'id': 9, 'is_finished': False, 'job': 'adding new tests', 'start_date': '2022-03-05 21:45:48', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:47:47', 'id': 10, 'is_finished': False, 'job': 'adding new tests 2 3 4', 'start_date': '2022-03-05 21:47:47', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:48:01', 'id': 11, 'is_finished': False, 'job': 'adding new tests 2 3 4', 'start_date': '2022-03-05 21:48:01', 'team_leader': 1, 'work_size': 11}, {'collaborators': '2, 5', 'end_date': '2022-03-05 21:48:42', 'id': 12, 'is_finished': False, 'job': 'adding new tests 2 3 4', 'start_date': '2022-03-05 21:48:42', 'team_leader': 1, 'work_size': 11}]}
    '''