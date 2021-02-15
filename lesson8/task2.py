'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''


class ZeroDivision(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroDivision

        return Number(float(self) / float(other))


try:
    dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
    print(dividend / divider)
except ZeroDivision as e:
    print(e)
except ValueError as e:
    print(e)


# class DivisionZero:
#     def __init__(self, divider, dividend):
#         self.divider = divider
#         self.dividend = dividend
#
#     @staticmethod
#     def divide_null(divider, dividend):
#         try:
#             return divider / dividend
#         except:
#             return f"Деление на ноль недопустимо"
#
#
# div = DivisionZero(10, 100)
# print(DivisionZero.divide_null(10, 0))
# print(DivisionZero.divide_null(10, 0.1))
# print(div.divide_null(100, 0))
