import re

html = "Курс евро на сегодня 81,2318, курс евро на завтра 84,4352"
match = re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)  # флаг IGNORECASE позволяет искать в другом регистре
rate = match.group(1)
print(rate)

match = re.search(r'Евро\D+(\d+,\d+)', html)  # без флага IGNORECASE не нашли данные
print(match is None)

print(re.search(r'Евро.*(\d+,\d+)', html, re.IGNORECASE).group(1))  # 4,4352

print(re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE).group(1))  # 81,2318

print(re.findall(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE))  # ['81,2318', '84,4352']

print(re.findall(r'Евро\D+\d+,\d+', html, re.IGNORECASE))  # ['евро на сегодня 81,2318', 'евро на завтра 84,4352']

print(re.findall(r'Евро\D+(\d+),(\d+)', html, re.IGNORECASE))  # [('81', '2318'), ('84', '4352')]

print(re.findall(r'Евро\D+((\d+),(\d+))', html, re.IGNORECASE))  # [('81,2318', '81', '2318'), ('84,4352', '84', '4352')]


