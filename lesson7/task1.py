'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = [(m_rows, len(row)) for row in self.__matrix]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])

    def __add__(self, other):

        if self.__matrix_size != other.__matrix_size:
            return "Матрицы разные"

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([a, b]) for a, b in zip(*item)])

        return Matrix(result)


matrix1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
print(matrix1, '\n')

matrix2 = Matrix([[10, 20, 30], [30, 40, 50], [50, 60, 70]])
print(matrix2, '\n')

print(matrix1 + matrix2)
