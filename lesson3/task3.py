'''
3.Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
'''


def my_try(x, y, z):
    a = 0
    if x >= y <= z:
        a = y
    elif y >= x <= z:
        a = x
    elif y >= z <= x:
        a = z
    sums = x + z + y - a

    print(sums)


my_try(1, 4, 1)
