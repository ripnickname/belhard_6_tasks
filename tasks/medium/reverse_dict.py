"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(key_value_dict: dict):
    new_dictionary = dict(zip(key_value_dict.values(), key_value_dict.keys()))
    return new_dictionary