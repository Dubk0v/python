'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

print(f'Расчёт заработной платы {float(argv[1]) * float(argv[2]) + int(argv[3])} y.e.')

# time, pay_rate, bonus = argv[1:]
# salary = time * pay_rate + bonus
# print(f'Расчёт заработной платы {salary} y.e.')


# если переменая типа time=8
# time = float(argv[1][argv[1].find('=')+1:])
# pay_rate = float(argv[2][argv[2].find('=')+1:])
# bonus = int(argv[3][argv[3].find('=')+1:])
# salary = time * pay_rate + bonus
# print(f'Расчёт заработной платы {salary} y.e.')

