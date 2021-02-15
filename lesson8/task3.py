'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание:
длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка:
для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
(не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''


class NumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []

while True:
    ask = input("Введите целое число для заполнения списка, или 'stop' для выхода: ")

    if ask == "stop":
        break

    try:
        if not ask.isdigit():
            raise NumberError(f"'{ask}' не соответствует запросу, введите целое число")

        my_list.append(int(ask))
    except NumberError as e:
        print(e)

print(my_list)

