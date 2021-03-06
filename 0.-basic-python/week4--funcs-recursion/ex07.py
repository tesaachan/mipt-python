"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def sum(a, b):
    if (a > 0):
        return 1 + sum(a-1, b)
    if (b > 0):
        return 1 + sum(a, b-1)
    else:
        return 0

a = int(input())
b = int(input())
print(sum(a, b))
