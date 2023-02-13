#  Напишите программу со статическим методом, аргументом которому передается
# целочисленный массив, а результатом возвращается среднее значение для элементов
# массива (сумма значений элементов, деленная на количество элементов в массиве).

import numpy

class Lab6Ex8:

    @staticmethod
    def get_argValue(value):
        return round(numpy.mean(value), 1)

a = Lab6Ex8()

userValue = list(map(int, input("Введите целочисленный массив: ").split()))

print(a.get_argValue(userValue))
