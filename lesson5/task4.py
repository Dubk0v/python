'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus = ['Один', 'Два', 'Три', 'Четыре']

with open('task4.txt', 'r') as eng:
    eng_list = []
    for line in eng:
        eng_list.append(line.split())
    for i, key in enumerate(eng_list):
        key[0] = rus[i]
with open('task4-1.txt', 'w') as edit:
    for edit_list in eng_list:
        edit.writelines(f'{" ".join(edit_list)} \n')
