from bs4 import BeautifulSoup
from decimal import Decimal
import requests



def convert(amount, cur_from, cur_to, date):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(date))
    soup = BeautifulSoup(response.content, 'xml')


    if cur_from != 'RUR':  # перевод валюты в рубли
        nominal_1 = Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string.replace(',', '.'))  # поиск номинала
        val = Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Value').string.replace(',', '.'))  # поиск значения в рублях
        amount = amount * val / nominal_1

    if cur_to == 'RUR':
        pass
    else:
        nominal_2 = Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string.replace(',', '.'))  # поиск номинала
        val2 = Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Value').string.replace(',', '.'))  # поиск значения в рублях
        amount = amount / val2 * nominal_2


    print(amount.quantize(Decimal("1.0000")))


convert(Decimal("1000"), 'USD', 'RUR', "23/07/2020")
