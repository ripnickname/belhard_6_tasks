"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def rec_func(n: int):
    if n == 0:
        return 0
    if n > 0:
        float = n % 10
        result = float + rec_func(n // 10)
        return result