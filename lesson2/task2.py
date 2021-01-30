'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

ask_list = list(input(':'))

if len(ask_list) % 2 == 0:
    print(ask_list)
    ask_list[::2], ask_list[1::2] = ask_list[1::2], ask_list[::2]
    print(ask_list)
else:
    print(ask_list)
    al = ask_list.pop()
    ask_list[::2], ask_list[1::2] = ask_list[1::2], ask_list[::2]
    ask_list.append(al)
    print(ask_list)

