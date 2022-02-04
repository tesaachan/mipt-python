"""
Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1. 
Алгоритм должен иметь сложность порядка корня квадратного из n.

Примечание: Если у числа n нет делителя не превосходящего корня из n, то число n — простое и ответом будет само число n. 
У всех составных чисел обязательно есть делители, отличные от единицы и не превосходящие корня из n.
"""


def MinDivisor(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return i
        i += 1

    return n


n = int(input())
mindiv = MinDivisor(n)
print(mindiv)
