'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def my_func(a, b):

    try:
        c = int(a) / int(b)
        print(c)
    except ZeroDivisionError:
        print('На 0 делить нельзя!!!')
    except ValueError:
        print('Введи число!!!')


x = input('x:')
y = input('y:')
my_func(x, y)
