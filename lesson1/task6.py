print('---')

start = 2
finish = 3
day = 1
while start <= finish:
    start += ((start * 10) / 100)
    day += 1
print(f'Спортсмен на {day} день достиг заданный результат' , '%.2f' % start , 'км.')

print('---')