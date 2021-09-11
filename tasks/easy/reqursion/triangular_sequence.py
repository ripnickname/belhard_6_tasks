"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, x=1):
    if n == 0:
        return 0
    if n == 1:
        print(1)
    if x < n + 1:
        print(str(x) * x)
        triangular_sequence(n, x + 1)


triangular_sequence(6)