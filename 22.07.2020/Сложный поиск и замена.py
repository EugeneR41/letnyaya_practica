import re

nicknames = ['sUr_h4XX0r', 'alёna', 'ivab ivanovich']
reg = re.compile(r'^\w+$', re.ASCII)
for nick in nicknames:
    print('{} nickname: "{}"'.format(
        'valid' if reg.match(nick) else 'invalid',
        nick
    ))  # valid nickname: "sUr_h4XX0r"
    # invalid nickname: "alёna"
    # invalid nickname: "ivab ivanovich"

text = (
    'Анна и Лена загорали на берегу океана, '
    'когда к ним подошли Яна и ПОЛИНА Ильнар'
)

print(re.findall(r'\b[А-Я]\w*(?:на|НА)\b', text))  # ['Анна', 'Лена', 'Яна', 'ПОЛИНА']

text = "Как защитить металл от процесса коррозии?"

print(re.findall(r'(\w)\1', text))  # ['л', 'с', 'р', 'и']
print(re.sub(r'а', '?', text))  # К?к з?щитить мет?лл от процесс? коррозии?
print(re.sub(r'(\w)\1', lambda r: r.group(0).upper(), text))  # Как защитить метаЛЛ от процеССа коРРозИИ?
print(re.sub(r'\b(\w*(\w)\2\w*)\b', r'[\1]', text))  # Как защитить [металл] от [процесса] [коррозии]?
