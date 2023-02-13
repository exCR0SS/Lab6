# Напишите программу со статическим методом, аргументом которому передастся
# символьный массив, а результатом возвращается ссылка на целочисленным массив,
# состоящий из кодов символов из массива- аргумента.


class Lab6Ex7:


    @staticmethod
    def get_charArr(userArr):
        resArr = []

        for i in range(len(userArr)):
            resArr.append(ord(userArr[i]))
        return resArr


a = Lab6Ex7()
userArr = list(map(str, input("Введите массив символов: ").split()))
print(a.get_charArr(userArr))
        