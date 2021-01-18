print('---')

number = int(input('Введите время в секундах: '))
hours = number // 3600
h = number % 3600
minutes = h // 60
seconds = h % 60
print(f'Время - {hours:02} : {minutes:02} : {seconds:02}')

print('---')
