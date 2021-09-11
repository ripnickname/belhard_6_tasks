"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(func):
        def wrapper(*args, **kwargs):
            print("Выполняем {func.__name__} c args: {args} и {kwargs}")
            result = func(*args, **kwargs)
            print("Выполнено {func.__name__}")
            return result
        return wrapper


@log_decorator
def hello(name: str):
    print(f"Привет, {name}")

hello("Паша")