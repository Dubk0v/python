'''
Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для городского траснспорта "{self.name}" - {self.speed} км/ч')

        if self.speed > 40:
            return f'{self.speed} км/ч - данная скорость привышает допустимую для городского траснспорта'
        else:
            return f'{self.speed} км/ч - Допустимая сокорость для городского траснспорта'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для рабочего траснспорта "{self.name}" - {self.speed} км/ч')

        if self.speed > 60:
            return f'{self.speed} км/ч - Скорость выше допустимой для рабочего траснспорта'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} обычная машина'


ferrari = SportCar(100, 'Красная', 'Феррари', False)
hyundai = TownCar(30, 'Желтая', 'Хондай', False)
lada = WorkCar(70, 'Серая', 'Лада', True)
dodge = PoliceCar(110, 'Черная', 'Додж', True)
print(lada.turn_left())
print(f'Прежде чем {hyundai.turn_right()}, {ferrari.stop()}')
print(f'{lada.go()} со скоростью - {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f'{ferrari.name} полицейский автомобиль? {ferrari.is_police}')
print(f'{lada.name} полицейский автомобиль? {lada.is_police}')
print(f'{ferrari.show_speed()}')
print(f'{hyundai.show_speed()}')
print(dodge.police())
print(dodge.show_speed())
