import sys
from fileinput import filename
from typing import Generator, Any


def filter_by_currency():
    pass




transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# def filter_by_currency(my_list, my_filter):
#     new_iter = filter(lambda x: x[my_filter], my_list)
#     # print(new_iter)
#
#
# # usd_transactions = filter_by_currency(transactions, "USD")
# print(list(filter_by_currency))
# for x in range(2):
#     print(list(usd_transactions))


# def filter_by_currency(transactions: list, currency_code: str = "USD") -> Any:
#     """Функция выдает список транзакции, где валюта соответствует заданной."""
    # if transactions == []:
    #     sys.exit("Нет транзакций")
    # for i in transactions:
    #     if i.get("operationAmount").get("currency").get("code") != currency_code:
    #         sys.exit("В транзакциях нет такого кода")
    #     elif i.get("operationAmount").get("currency").get("code") == currency_code:
    #         yield i

    # try:
    #     for i in transactions:
    #         if i.get('operationAmount').get('currency').get('code') == currency_code:
    #             yield i
    # except StopIteration:
    #     if transactions == []:
    #         return 'Нет транзакций'

    # if transactions == []:
    #     yield ("Нет транзакций")
    # for i in transactions:
    #     if i.get("operationAmount").get("currency").get("code") == currency_code:
    #         yield i
    #     elif i.get("operationAmount").get("currency").get("code") != currency_code:
    #         yield "Транзакции с таким кодом нет"

###############################################
# def filter_by_currency(transactions, currency_code: str="USD"):
#     """ Функция выдает транзакции, где валюта операции соответствует заданной."""
#     try:
#         for i in transactions:
#             if i.get('operationAmount').get('currency').get('code') == currency_code:
#                 yield i
#     except StopIteration:
#         if transactions == []:
#             return 'Нет транзакций'
# ##################################################
#
# usd_transactions = filter_by_currency(transactions, "USD")
# for i in range(len(transactions)):
#     print(usd_transactions)


# def filter_by_currency(transactions: list, currency_code: str = "USD") -> Generator[Any, Any, Any]:
#     """Функция выдает транзакции, где валюта операции соответствует заданной."""
#     if transactions == []:
#         yield ("Нет транзакций")
#     for i in transactions:
#         if i["operationAmount"]["currency"]["code"] == currency_code:
#             yield i
#         else:
#             print ("В транзакциях нет такого кода")



# def filter_by_currency(transactions: list, currency_code: str = "USD") -> Generator[Any, Any, Any]:
#     """Функция выдает транзакции, где валюта операции соответствует заданной."""
#
#     if transactions == []:
#         sys.exit("Нет транзакций")
#     for i in transactions:
#         if i["operationAmount"]["currency"]["code"] == currency_code:
#             yield i
#         else:
#             sys.exit("В транзакциях нет такого кода")
#
#
# usd_transactions = filter_by_currency(transactions, "USD")
# for i in range(len(transactions)):
#     print(next(usd_transactions))
###############################################################3

# def my_dec(kol, sim="!"):
#     def my_rounding(function):
#         def rounding(*args, **kwargs):
#             result = function(*args, **kwargs)
#             res2 = result.split()
#             print(f"Перед обработкой: {res2}")
#             count = []
#             for i in res2:
#                 if len(i) > kol:
#                     i = i[:kol]+sim
#                     count.append(i)
#                 else:
#                     count.append(i)
#             return ' '.join(count)
#         return rounding
#     return my_rounding
#
#
# @my_dec(4, '!')
# def add_one(x):
#     return x
#
# y = add_one("hellolldl worlder4rt ijwuih kjabhfiyasgi")
# print("После обработки:", y)


###############################################################

# def check_round(precision):
#     def check_integers(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             # Проверка на тип с использованием type()
#             if type(result) == float:
#                 return round(result, precision)
#             elif type(result) in (list, tuple):
#                 rounded = [round(x, precision) if type(x) == float else x for x in result]
#                 # Возвращаем тот же тип, что и исходный (list или tuple)
#                 return type(result)(rounded)
#             else:
#                 return result
#         return wrapper
#     return check_integers
#
# @check_round(1)
# def calc(x):
#     my_list = []
#     list = [2,5,67]
#     for i in list:
#         i *= x
#         my_list.append(i)
#     return my_list
# res = calc(3.6)
# print(res)

#################################################################

from functools import wraps


def log(filename=None):
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def dekorator(func: Any):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not filename:
                print(f'{func.__name__} started')
                print(type(func))
                try:
                    func(*args, **kwargs)
                    print(f'{func.__name__} ok')
                    print(f'{func.__name__} finished')
                except Exception as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            else:
                try:
                    func(*args, **kwargs)
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} ok')
                except Exception as e:
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            # return result
        return wrapper
    return dekorator


@log()
def summ(x, y):

    return x / y

res = summ(5,"b")
print(res)
# def get_mask_account(number: str) -> str:
#     """Функция создания маски типа **хххх для числа"""
#
#     if len(str(number)) < 20:
#         return "не корректно введен номер"
#     else:
#         number_str = str(number)
#         last_chars = number_str[-4:]
#         return f"**{last_chars}"
#
#
# print(get_mask_account("12345678901234567890"))