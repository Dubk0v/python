print('---')

proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
profit = proceeds - costs
cash = (proceeds / costs) * 100
if cash > 0:
    print('Фирма рентабельна.')
    print(f'Прибыль фирмы: {profit}')
    workers = int(input('Сколько сотрудников в фирме: '))
    print(f'Прибыль на каждого сотрудника: {profit/ workers:.2f}')
elif cash == 0:
    print('Фирма однодневка.')
else:
    print('Фирма не рентабельна.')

print('---')