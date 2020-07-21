import requests  # Подключение библиотеки requests
from collections import Counter  # Импортирование counter из библиотеки collections для подсчета людей с одинаковым возрастом

ACCESS_TOKEN = "113e093d113e093d113e093db2114d157f1113e113e093d4e2b0ecd13c532e43f1cc7d5"  # Сервисный ключ
API_VER = '5.89'  # Версия api
FRIENDS = []  # Список друзей


def calc_age(uid):
    # Запрос данных о пользователе т.к. в запросе друзей нужен айди, а пользователь может ввести никнейм. Поэтому надо конвертировать ник в айди
    x = requests.get("https://api.vk.com/method/users.get?v={}&access_token={}&user_ids={}".format(API_VER, ACCESS_TOKEN, uid))
    ID = x.json()['response'][0]['id']  # Добавляем айди
    global temp, keys
    # Запрос данных о друзьях
    r = requests.get('https://api.vk.com/method/friends.get?v={}&access_token={}&user_id={}&fields=bdate'.format(API_VER, ACCESS_TOKEN, ID))

    for i in range(r.json()['response']['count']):  # От 0 до количества друзей
        try:  # Выполняем инструкцию, которая может породить исключение
            if (r.json()['response']['items'][i]['bdate']).count(".") == 2:  # Подсчет двух точек, т.к. у некоторых нет даты рождения или она состоит только из дня и месяца
                temp = int(r.json()['response']['items'][i]['bdate'][::-1][:4][::-1])  # Вычисление года
                temp = 2020 - temp  # Вычисление возраста
                FRIENDS.append(temp)  # Добавляем в список возраст друга
        except BaseException:  # Если исключение, то ничего не делать
            pass

    YEARS = (list(Counter(sorted(FRIENDS)).most_common()))  # подсчет друзей с одинаковым возрастом
    return YEARS
# Вывод (в моем случае)
# [(19, 17), (18, 3), (20, 2), (21, 2), (30, 1), (45, 1)]


if __name__ == '__main__':
    res = calc_age('eugene_41')  # Id пользователя или никнейм
    print(res)
