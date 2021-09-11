"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(arg1: set, arg2: set, arg3: set, symmetric=False):
    if symmetric is True:
        result = arg1 ^ arg2 ^ arg3
    else:
        result = arg1 - arg2 - arg3
    return result
