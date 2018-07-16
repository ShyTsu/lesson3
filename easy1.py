# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def info_about_humans(name, age, town):

    text = '{}, {} год(а) проживает в городе {}'
    print(text.format(name, age, town))


x = ['Иван', 27, 'Москва']
info_about_humans(*x)


#ИЛИ ТАК
#
#
# def info_about_humans(name, age, town):
#
#     text = '{}, {} год(а) проживает в городе {}'
#     print(text.format(name, age, town))
#
#
# name = input('Введите Ваше имя: ')
# age = input('Введите Ваш возраст: ')
# town = input('Введите город проживания: ')
#
# info_about_humans(name, age, town)