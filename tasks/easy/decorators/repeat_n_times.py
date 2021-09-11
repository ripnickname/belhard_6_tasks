"""
Написать функцию bang, которая печатает "Boom"
Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


from functools import wraps


def repeat_n_times(n):
    def decorate(bang):
        @wraps(bang)
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = bang(*args, **kwargs)
            return result
        return wrapper
    return decorate


@repeat_n_times(10)
def say(message):
    print(message)


say('Boom')