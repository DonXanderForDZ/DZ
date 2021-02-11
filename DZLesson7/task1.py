"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                self.list_1[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))

    def __str__(self):
        return str('\n'.join(['t'.join([str(j) for j in i]) for i in self.list_1]))


ln_matx = int(input('Введите количество столбцов матриц: '))
ht_matx = int(input('Введите количество строк матриц: '))
matx1 = []
matx2 = []
n = 0
while n < ht_matx:
    k = 0
    list1 = []
    while k < ln_matx:
        el = int(input('Введите элемент первой матрицы: '))
        list1.append(el)
        k += 1
    matx1.append(list1)
    n += 1
n = 0
while n < ht_matx:
    k = 0
    list2 = []
    while k < ln_matx:
        el = int(input('Введите элемент второй матрицы: '))
        list2.append(el)
        k += 1
    matx2.append(list2)
    n += 1

my_matrix = Matrix(matx1, matx2)

print(my_matrix.__add__())
