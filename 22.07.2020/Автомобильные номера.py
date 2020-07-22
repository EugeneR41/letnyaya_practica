import re


text = '''
Автомобиль с номером A123BC77 подрезал автомобиль
K654HE197, спровоцировал ДТП с участием еще двух
иномарок с номерами M542OP777 и O007OO77
'''

pattern = r'[ABEKMHOPCTYX]\d{3}[ABEKMHOPCTYX]{2}\d{2,3}'
print(re.findall(pattern, text))  # ['A123BC77', 'K654HE197', 'M542OP777', 'O007OO77']
