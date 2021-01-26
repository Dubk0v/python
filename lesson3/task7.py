'''
7. Продолжить работу над заданием.
В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
'''


def all_title(sentence):
    words = []
    for word in sentence.split():
        if not word.isalpha():
            for ind, i in enumerate(word):
                if not i.isalpha():
                    continue
                else:
                    word = word[:ind] + word[ind].upper() + word[ind + 1:]
                    words.append(word)
                    break
        else:
            word = word[0].upper() + word[1:]
            words.append(word)
    return ' '.join(list(words))
    #return sentence.title()


ask = input('Введите слова: ').lower()
print(all_title(ask))
