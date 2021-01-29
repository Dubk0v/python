'''
Создать текстовый файл (не программно),
сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

symbols = []
with open('task2.txt', 'r') as fp:
    x = 0
    y = 0
    for line in fp:
        x += 1
        y = line.count(' ')
        symbols.append(x)
        symbols.append(y)

print(x, y, symbols)
        # for word in line.split():
        #     y += 1
        #     print(word)
        #     print(x)
        #     print(y)
