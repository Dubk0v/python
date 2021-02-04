'''
Реализовать класс Stationery (канцелярская принадлежность).

определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    # title = str
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки: {self.title}')
        # return 'Запуск отрисовки: {self.title}'


class Pen(Stationery):
    # title = 'ручка'

    def draw(self):
        # print(f'Пишет - {self.title}')
        return f'Пишет - {self.title}'


class Pencil(Stationery):
    # title = 'карандаш'

    def draw(self):
        # print(f'Чертит - {self.title}')
        return f'Чертит - {self.title}'


class Handle(Stationery):
    # title = 'маркер'

    def draw(self):
        # print(f'Рисует - {self.title}')
        return f'Рисует - {self.title}'


# pen = Pen()
pen = Pen('ручка')
# pen.draw()
print(pen.draw())
# pencil = Pencil()
pencil = Pencil('карандаш')
# pencil.draw()
print(pencil.draw())
# handle = Handle()
handle = Handle('маркер')
# handle.draw()
print(handle.draw())
