"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 20, 3, 40, 5, 60]


def common_numbers(list1, list2) -> list:
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    result.sort(reverse=True)
    return result