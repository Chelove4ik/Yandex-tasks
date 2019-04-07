from requests import get, post, delete, put

print(get('http://localhost:8080/users').json())
print(get('http://localhost:8080/users/3').json())
print(get('http://localhost:8080/users/8').json())  # ошибка
print(get('http://localhost:8080/users/q').json())  # ошибка
print()
print(post('http://localhost:8080/users').json())  # ошибка
print(post('http://localhost:8080/users',
           json={'title': 'Заголовок'}).json())  # ошибка
print(post('http://localhost:8080/users',
           json={'user_name': 'qwerty',
                 'password': '101001001'}).json())
print()
print(delete('http://localhost:8080/users/8').json())  # ошибка
print(delete('http://localhost:8080/users/4').json())

print(put('http://localhost:8080/users/1', json={'password': 123}).json())
print(put('http://localhost:8080/users/1', json={'password': 123, 'id': 'qwer'}).json())
print(put('http://localhost:8080/users/1', json={'user_id': 123}).json())  # ошибка
