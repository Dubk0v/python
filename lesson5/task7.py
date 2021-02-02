'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''
from json import dumps

results = [{}, {}]
with open('task7.txt', 'r', encoding='utf-8') as fhs:
    for line in fhs.readlines():
        firma, tmp, proceeds, costs = line.split()
        results[0][firma] = int(proceeds) - int(costs)
divisor = [profit for profit in results[0].values() if profit > 0]
results[1]['average_profit'] = sum(divisor) / len(divisor)
# results[1]['average_profit'] = round(sum(profit for profit in results[0].values() if profit > 0) / len(divisor))

with open('task7.json', "w", encoding='utf-8') as fhd:
    fhd.write(dumps(results))
