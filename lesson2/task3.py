'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

list_of_seasons = ['лето', 'зима', 'весна', 'осень']
dict_of_seasons = {1: 'лето', 2: 'зима', 3: 'весна', 4: 'осень'}
month = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
number = int(input('Введите месяц в виде целого числа от 1 до 12: '))
while 0 <= number <= 12:

    if 3 <= number <= 5:
        print(f'{month[number - 1]} относится к {list_of_seasons[2]}')
    elif 6 <= number <= 8:
        print(f'{month[number - 1]} относится к {list_of_seasons[0]}')
    elif 9 <= number <= 11:
        print(f'{month[number - 1]} относится к {list_of_seasons[3]}')
    else:
        print(f'{month[number - 1]} относится к {list_of_seasons[1]}')

number = int(input('Введите месяц в виде целого числа от 1 до 12: '))
