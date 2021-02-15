'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


# class MyComplex:
#     def __init__(self, a, b):
#         self.__complex = complex(a, b)
#
#     def __add__(self, other):
#         if isinstance(other, MyComplex):
#             other = other.__complex
#
#         complex_ = self.__complex + other
#         return MyComplex(complex_.a, int(complex_.b))
#
#     def __mul__(self, other):
#         if isinstance(other, MyComplex):
#             other = other.__complex
#
#         complex_ = self.__complex * other
#         return MyComplex(complex_.a, int(complex_.b))
#
#     def __str__(self):
#         return self.__complex.__str__()
#
#
# c1 = MyComplex(10, -5)
# c2 = MyComplex(30, 15)
#
# print(c1 + c2, complex(10, -5) + complex(30, 15))
# print(c1 * c2, complex(10, -5) * complex(30, 15))


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} * {self.b * other.a}'

    def __str__(self):
        return f'z = {self.a} + {self.b}'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
