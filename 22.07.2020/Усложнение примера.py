import re
html = """
Курс евро на сегодня  (15 января)
составляет 81,2318"""
match = re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
rate = match.group(1)
print(rate)  # AttributeError: 'NoneType' object has no attribute 'group'

match = re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE)
rate = match.group(1)
print(rate)  # AttributeError: 'NoneType' object has no attribute 'group'

match = re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE | re.DOTALL)  # переключает регулярные выражения в режим, когда точка обозначает любой символ
rate = match.group(1)
print(rate)  # 81,2318
