from requests import get

print(get('http://localhost:5000/news').json())
