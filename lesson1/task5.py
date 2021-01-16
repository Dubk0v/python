print('---')

proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
cash = proceeds / costs
if proceeds > costs:
    print('Фирма рентабельна.')
    print(f'Прибыль фирмы: {cash:.2f}')
    workers = int(input('Сколько сотрудников в фирме: '))
    print(f'Прибыль на каждого сотрудника: {cash / workers:.2f}')
elif proceeds == costs:
    print('Фирма однодневка.')
else:
    print('Фирма не рентабельна.')

print('---')