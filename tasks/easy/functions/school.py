"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(students, one_a):
    students = students[one_a] + 1
    return students


def decr_students(students, one_b):
    if students[one_b] > 0:
        students = students[one_b] - 1
    return students


def add_class(students, one_c):
    students.update({one_c: 0})
    return school_data


def remove_class(students, two_a):
    students.pop(two_a)
    return school_data


def calc_class(students):
    return sum(students.values())
