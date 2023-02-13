# Напишите программу со статическим методом, которому аргументом передается
# целочисленный массив и целое число. Результатом метод возвращает ссылку на новый
# массив, который получается из исходного массива (переданного первым аргументом
# методу), если в нем взять несколько начальных элементов. Количество элементов, которые
# нужно взять из исходного массива, определяются вторым аргументом метода. Если второй
# аргумент метода больше длины массива, переданного первым аргументом, то методом
# создается копия исходного массива и возвращается ссылка на эту копию.

import copy

class Lab6Ex6:

    @staticmethod
    def get_value(valueArray, value):
        resArray = []
        if value < len(valueArray):
            for i in range(value):
                resArray.append(copy.deepcopy(valueArray[i]))
        else:
            resArray = copy.deepcopy(valueArray)
        return resArray

a = Lab6Ex6()

userArr = list(map(int, input("Введите массив целых чисел: ").split()))
userValue = int(input("Введите число: "))

print(a.get_value(userArr, userValue))