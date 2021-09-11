"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


num = 5
