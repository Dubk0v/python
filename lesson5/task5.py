'''
Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

from random import randint
z = 0
nl = [randint(1, 100) for i in range(20)]
num_list = open('task5.txt', 'r+')
for edit_list in nl:
    num_list.writelines(f'{"".join(str(edit_list))} ')
pl = num_list.read().split()
for i in map(int, pl):
    z += i
print(f'сумма числел в файле: {z}')
num_list.close()