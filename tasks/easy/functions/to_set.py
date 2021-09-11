"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(some_list: list):
    some_list_2 = set(some_list)
    print(some_list_2, len(some_list_2))
    return some_list_2, len(some_list_2)
