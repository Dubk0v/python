'''
Создать текстовый файл (не программно),
сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

with open('task2.txt', 'r') as fp:
    x = 0
    for line in fp:
        y = 0
        x += 1
        for word in line.split():
            if word != ' ' or word != '\n':
                y += line.count(word)
        else:
            print(f'в {x}й строке {y} слова')
