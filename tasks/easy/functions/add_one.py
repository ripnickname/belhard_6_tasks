"""
Написать функцию-замыкание add_numb, которая при создании принимает число,
которое нужно прибавлять к другому числу.

После присвоения переменной она должна принимать другое число и прибавлять к
нему первое

Пример:

add_two = add_numb(2)
add_two(3)  # 5

add_three = add_numb(3)
add_three(3) # 6
"""


def add_numb(num1, num2):
    result = num1 + num2
    print(result)
    return result
