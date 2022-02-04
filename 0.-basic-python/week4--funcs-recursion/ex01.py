"""
Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
которая не содержит инструкции if, а использует стандартную функцию min от двух чисел.
Считайте четыре целых числа и выведите их минимум.
"""


def min4(a, b, c, d):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    if d < min:
        min = d
    return min


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
