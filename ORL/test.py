from requests import get, post, delete


print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/2').json())
print(get('http://localhost:8080/api/v2/users/6').json())
print(get('http://localhost:8080/api/v2/users/q').json())
print(post('http://localhost:8080/api/v2/users').json())
print(post('http://localhost:8080/api/v2/users', json={'name': 'Andy Weir'}).json())
print(post('http://localhost:8080/api/v2/users', json={
    'name': 'Andy Weir',
    'about': 'astronaut',
    'email': 'us4@mars.org',
    'hashed_password': 'pbkdf2:sha256:260000$PWzNK4Vm1qsjK4n5$bda98e3e3fc43a24bd4777b7983192095bb22979d3d5d8e424083cb3cbe9c22a',
    'city_from': 'London'}).json())
print(delete('http://localhost:8080/api/v2/users/999').json()) # пользователя с id = 999 нет в базе
print(delete('http://localhost:8080/api/v2/users/3').json())