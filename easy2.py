# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def what_more(maxnumber):
    x = int(input('Введите число для x: '))
    y = int(input('Введите число для y: '))
    z = int(input('Введите число для z: '))
    text = '{} - самое большое число'
    maxnumber = max(x, y, z)
    print(text.format(maxnumber))


what_more('')


# ИЛИ ТАК
#
#
# def what_more(x, y, z):
#     return max(x, y, z)
#
#
# print(what_more(11, -7, 31))







