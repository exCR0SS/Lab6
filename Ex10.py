# Напишите программу со статическим методом, аргументом которому передается
# произвольное количество целочисленных аргументов. Результатом метод возвращает
# массив из двух элементов: это значения наибольшего и наименьшего значений среди
# аргументов, переданных методу

class Lab6Ex10:

    @staticmethod
    def get_arr(userArr):
        resArr = []
        resArr.append(max(userArr))
        resArr.append(min(userArr))
        return resArr


a = Lab6Ex10()

userArr = list(map(int, input("Введите массив чисел через пробел: ").split()))
# userArr = [1, 3, 5, 6, 8, 11, 24]
print(a.get_arr(userArr))
