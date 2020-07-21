import requests  # импортирование библиотеки requests

# Make a Request
r = requests.get('http://httpbin.org/get')  # get запрос
print(r.text)

# Вывод:
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14eeb7-c593c0c04e0eb4e0e9d73900"
#   },
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/get"
# }


r = requests.post('http://httpbin.org/post')  # post запрос
print(r.text)

# Вывод:
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "0",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14f171-cfd99efa990607aada9c5e8e"
#   },
#   "json": null,
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/post"
# }

# Passing Parameters
payload = {'key1': 'value1', 'key2': 'value2'}  # словарь/параметры
r = requests.get('http://httpbin.org/get', params=payload)  # get запрос с параметрами
print(r.text)

# Вывод
# {
#   "args": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14f171-a6026d08f63e3120363665d0"
#   },
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/get?key1=value1&key2=value2"
# }

r = requests.put('http://httpbin.org/put', data={'key': 'value'})  # передача данных в post/put, patсh запросах
print(r.text)

# Вывод
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "key": "value"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "9",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14f172-03defc649d0c4466fd2d6209"
#   },
#   "json": null,
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/put"
# }


import json  # импорт библиотеки json

url = 'http://httpbin.org/post'
r = requests.post(url, data=json.dumps({'key': 'value'}))  # создание json'а вручную и передача в поле data
r = requests.post(url, json={'key': 'value'})  # встроенный механизм в библиотеке requests, передача в поле json
print(r.text)

# Вывод
# {
#   "args": {},
#   "data": "{\"key\": \"value\"}",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "16",
#     "Content-Type": "application/json",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14f4f7-587af07efc46607cb0a679e4"
#   },
#   "json": {
#     "key": "value"
#   },
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/post"
# }

# POST a Multipart File
# Передача файла на сервер
url = 'http://httpbin.org/post'
files = {'file': ('test.txt', open('/Users/Eugene/Desktop/test.txt',
                                   'rb'))}  # Словарь, где ключ это ключ по которому мы можем получить файл на сервере
r = requests.post(url, files=files)  # В методе requests в поле files передаем нашу переменную files, объявленную ранее
print(r.text)

# Вывод
# {
#   "args": {},
#   "data": "",
#   "files": {
#     "file": "proverka"  # текст в файле
#   },
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "152",
#     "Content-Type": "multipart/form-data; boundary=48cd2516f41a75ec95b525df1fcb02aa",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14f778-0e4128eae52accd9b46e223b"
#   },
#   "json": null,
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/post"
# }


# Headers
# Передача заголовков
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
print(r.text)

# Вывод
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "my-app/0.0.1",  # Передали User-Agent
#     "X-Amzn-Trace-Id": "Root=1-5f14f84a-3893ff6c598dffaca163e5f4"
#   },
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/get"
# }


# Response Content
r = requests.get('http://httpbin.org/get')
print(type(r.text), r.text)  # Вернет данные с типом string
print(type(r.content), r.content)  # Вернет массив байт
print(type(r.json()), r.json())  # Вернет словарь

# Вывод
# <class 'str'> {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",                                                # Это вернул text
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f14f91a-49ca7c634cbfebcccd8508f4"
#   },
#   "origin": "77.82.14.58",
#   "url": "http://httpbin.org/get"
# }
#

# Это вернул content
# <class 'bytes'> b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n
# "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n
# "User-Agent": "python-requests/2.24.0", \n
# "X-Amzn-Trace-Id": "Root=1-5f14f91a-49ca7c634cbfebcccd8508f4"\n  },
# \n  "origin": "77.82.14.58", \n  "url": "http://httpbin.org/get"\n}\n'

# Это вернул json
# <class 'dict'> {'args': {}, 'headers': {'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org',
# 'User-Agent': 'python-requests/2.24.0', 'X-Amzn-Trace-Id':
# 'Root=1-5f14f91a-49ca7c634cbfebcccd8508f4'}, 'origin':
# '77.82.14.58', 'url': 'http://httpbin.org/get'}


# Response Status Codes
print(r.status_code)  # Вернет статус
print(r.status_code == requests.codes.ok)  # Сравнения ответа на возвращение OK из библиотеки requests

# Вывод
# 200
# True

# Метод исключения raise_for_status
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()  # Вызов исключения

# Вывод
# 404
# Traceback (most recent call last):
#   File "C:/Users/Eugene/PycharmProjects/letnaya_practica/lecture_with_comments .py", line 222, in <module>
#     bad_r.raise_for_status()
#   File "C:\Users\Eugene\AppData\Local\Programs\Python\Python38-32\lib\site-packages\requests\models.py", line 941, in raise_for_status
#     raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error: NOT FOUND for url: http://httpbin.org/status/404  # Исключение


# Response Headers
print(r.headers)  # просмотр заголовка http ответа (вернет словарь)

# Вывод
# {'Date': 'Mon, 21 Jul 2020 02:08:20 GMT', 'Content-Type': 'application/json',
# 'Content-Length': '304', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0',
# 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}


# Redirection and History
r = requests.get('http://github.com')
print(r.url)  # Вернет не http, а https
print(r.status_code)  # Вернет 200
print(r.history)  # Вернет 301, т.к. нас перенаправили и сказали обращатся к https

# Вывод
# https://github.com/
# 200
# [<Response [301]>]

# Случай, когда мы запрещаем redirect
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)  # вернет 301(redirect)
print(r.history)  # ничего не вернет

# Вывод
# 301
# []


# Cookies данные которые передаются при каждом запросе

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

# Вывод
# {
#   "cookies": {
#     "cookies_are": "working"
#   }
# }


# Session Objects
s = requests.Session()  # после объявления сессии все следующие запросы будут выполняться с теми же параметрами, что и предыдущие
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)

# Вывод
# <RequestsCookieJar[<Cookie sessioncookie=123456789 for httpbin.org/>]>
# {
#   "cookies": {
#     "sessioncookie": "123456789"
#   }
# }


# С параметрами
s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)

# Вывод
# {
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-5f150056-1b10c5405d83a0bea797ae30",
#     "X-Test": "true",
#     "X-Test2": "true"
#   }
# }
