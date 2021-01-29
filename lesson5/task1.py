'''
Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''

# fp = open('task1.txt', 'w')
# line = input('Введите строку: ')
# while line:
#     fp.writelines(f'{line} \n')
#     line = input('Введите строку: ')
#     if not line:
#         break
# fp.close()

with open('task1.txt', 'w') as fp:
    line = input('Введите строку: ')
    while line:
        fp.writelines(f'{line} \n')
        line = input('Введите строку: ')
        if not line:
            break
