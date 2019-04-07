from requests import put, get

print(get('http://localhost:8080/news').json())

print(put('http://localhost:8080/news',
          json={'id': 15,
                'title': 'контент',
                'content': 'заголовок',
                'user_id': 1}).json())

print(get('http://localhost:8080/news').json())
