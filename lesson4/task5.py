'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
'''

from functools import reduce


def multiplication(el_prev, el):
    return el_prev * el


given_list = [el for el in range(100, 1001, 2)]
print(reduce(multiplication, given_list))
