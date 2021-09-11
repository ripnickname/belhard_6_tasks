"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(number):
    if number <= 0:
        return False
    elif number == 1 or number == 2:
        return True
    elif number > 2:
        other = number % 2
        number = number / 2
        if other == 0:
            return True
        else:
            return False
