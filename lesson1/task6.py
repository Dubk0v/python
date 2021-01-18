print('---')

start = int(input('Сколько пробежали в первый день: '))
finish = int(input('Сколько км. вы хотите пробежать ? '))
day = 1
while start <= finish:
    start += ((start * 10) / 100)
    day += 1
print(f'Спортсмен на {day} день достиг заданный результат - не менее {finish} км.')

print('---')