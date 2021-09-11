"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n):
    def closure(x):
        result = x * n
        print(result)
        return result
    return closure
