'''
6.Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
'''


def title(word):
    z = True
    while z:
        if not word.isalpha():
            word = input('Слово и нечего более: ')
        else:
            z = False
            #word = word.capitalize()
            #word = word.title()
            word = word[0].upper() + word[1:]
    return word


ask_word = input('Введите слово: ').lower()
print(title(ask_word))
