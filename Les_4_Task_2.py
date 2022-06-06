# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal?Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро

import requests


from requests import get, utils
from decimal import Decimal


response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    content = response.split("<Value ID=")
    for i in content:
        if code.upper() in i:
            # return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))
            return Decimal(i.replace("/", "").split("<Value>")[-2].replace(",", "."))




print(currency_rates("uSD"))
print(currency_rates("EURO"))       #вернет None т.к. неправильно написан код валюты
print(currency_rates("EUR"))
