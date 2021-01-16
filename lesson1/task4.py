print('---')

number = int(input('Введите число: '))
n = 0
while number > 0:
    if number % 10 > n:
        n = number % 10
    number = number // 10

print(f'Самая большая цифра: {n} в числе.')

print('---')