'''
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
'''


with open('task3.txt', 'r') as mfl:
    surname = []
    salary = []
    for line in mfl.read().split('\n'):
        if float(line.split()[1]) < 20000:
            surname.append(line.split()[0])
        salary.append(line.split()[1])
average_salary = (sum(map(float, salary)) / len(salary))

print(f'{surname} у них зарплата меньше 20000. средняя зарплата: {"%.2f" % average_salary}')
