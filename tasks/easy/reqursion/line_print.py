"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


some_list = [1, 2, [1, 2, [5, 7], 3], 8]


def line_print(list_checker: list, x=0):
    for i in list_checker:
        if isinstance(i, list):
            line_print(i, x + 1)
        else:
            t = '\t' * x
            print(f"{t}{i}")


if __name__ == "__main__":
    line_print(some_list)
