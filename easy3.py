# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def the_longest_line(*args):
    count = 0
    string = ''
    args = ['algorithmic', 'decoration', 'ocean', 'mercedes', 'literature']
    for x in args:
        if len(x) > count:
            count = len(x)
            string = x
    print(string)


the_longest_line()


