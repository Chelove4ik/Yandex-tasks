from requests import get, post, delete

print(get('http://localhost:8080/news').json())
print(get('http://localhost:8080/news/5').json())
print(get('http://localhost:8080/news/8').json())  # ошибка
print(get('http://localhost:8080/news/q').json())  # ошибка
print()
print(post('http://localhost:8080/news').json())  # ошибка
print(post('http://localhost:8080/news',
           json={'title': 'Заголовок'}).json())  # ошибка
print(post('http://localhost:8080/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1}).json())
print()
print(delete('http://localhost:8080/news/8').json())  # ошибка
print(delete('http://localhost:8080/news/11').json())
