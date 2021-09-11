"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def rec_func(n: int):
    if n == 0:
        return 0
    if n > 0:
        float_num = n % 10
        result = float_num + rec_func(n // 10)
        return result
