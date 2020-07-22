import requests  # Импортирование библиотеки requests
import re

result = requests.get("http://cbr.ru")  # Запрос на главную страницу ЦБ
html = result.text  # HTML код страницы
match = re.search(r'Евро\D+(\d+,\d+)', html)  # Поиск курса
rate = match.group(1)
print('Курс евро = ' + rate + ' р.')