"""
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите aⁿ, не используя циклы и стандартную функцию pow,
но используя рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
"""


def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * power(a, n-1)
    b = power(a, n/2)
    return b * b

a = float(input())
n = int(input())
print(power(a, n))
