'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''


class Textiles:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_c(self):
        return self.width / 6.5 + 0.5

    def get_s(self):
        return self.height * 2 + 0.3

    @property
    def get_full(self):
        return f'общий расход ткани: {round(self.get_c() + self.get_s())}'


class Coat(Textiles):
    def __init__(self, width):
        self.width = width
        self._c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'расход ткани на пальто: {self._c}'


class Suit(Textiles):
    def __init__(self, height):
        self.height = height
        self._s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'расход ткани на костюм: {self._s}'


coat = Coat(56)
suit = Suit(180)
print(coat)
print(suit)
print(Textiles(56, 180).get_full)
print(coat.get_c())
print(suit.get_s())
