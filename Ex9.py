# Напишите программу со статическим методом, аргументом которому передается
# одномерный символьный массив. В результате вызова метода элементы массива попарно
# меняются местами: первый — с последним, второй — с предпоследним и так далее.


class Lab6Ex9:


    @staticmethod
    def get_arr(userArr):
        resArr = []

        resArr.append(userArr[::-1])

        return resArr

a = Lab6Ex9()

userArr = list(map(str, input("Введите массив: ").split()))
# userArr = ['f', '4', 't', '6', 'g', 'r']
print(a.get_arr(userArr))