'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

from typing import List, Tuple, Union
from math import floor


class Number(int):
    def __str__(self):
        return f"{self:02}"


class Date:
    __date = ('day', 'month', 'year')

    def __init__(self, _date: str, /):
        fragments = _date.split('-')

        if not self.validate(*fragments):
            raise ValueError(f"{_date} Неправильный формат")

        self.day, self.month, self.year = self.transform(fragments)

    def __iter__(self):
        for dmy in self.__date:
            yield self.__getattribute__(dmy)

    @classmethod
    def transform(cls, date: Union[List[str], Tuple[str]]) -> List[Number]:
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date: Union[List[str], Tuple[str]]) -> bool:
        try:
            day, month, year = [int(i) for i in date]
        except TypeError:
            return False

        dmy = bool(not (year % 400 and year % 4) and year % 100)
        emd = 28 + (month + floor(month / 8)) % 2 + 2 % month + 2 * floor(1 / month)
        emd += dmy if month == 2 else 0

        return all([1 <= day <= emd, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


for date in ('01-12-2011', '01-12-1969', '29-02-2020', '29-02-2021'):
    try:
        print(Date(date))
    except ValueError as e:
        print(e)


# class Data:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-':
#                 my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2025 >= year >= 0:
#                     return f'OK'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
#
# today = Data('14 - 02 - 2021')
# print(today)
# print(Data.valid(1, 4, 2026))
# print(today.valid(1, 13, 2011))
# print(Data.valid(32, 4, 1988))
