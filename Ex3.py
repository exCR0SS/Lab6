# Напишите программу с классом, в котором есть статические методы, которым
# можно передавать произвольное количество целочисленных аргументов (или целочисленный массив). Методы, на основании переданных аргументов или массива,
# позволяют вычислить: наибольшее значение, наименьшее значение, а также среднее значение из набора чисел.


import numpy

class Lab6Ex3:

    def get_value(self, userLst):
        self.minValue = min(userLst)
        self.maxValue = max(userLst)
        self.avgArr = []

        for i in range(len(userLst)):
            self.avgArr.append(abs(numpy.mean(userLst) - userLst[i]))
        self.avgValue = userLst[self.avgArr.index(min(self.avgArr))]
        return self.minValue, self.maxValue, self.avgValue

userFunctional = Lab6Ex3()

userArr = list(map(int, input("Введите элементы массива через пробел: ").split()))
# userArr = [12, 14, 16, 18, 20]
minUserArr, maxUserArr, avgArr = userFunctional.get_value(userArr)
print(f"Минимальное значение: {minUserArr} \nМаксимальное значение: {maxUserArr}\nСреднее значение: {avgArr}")

