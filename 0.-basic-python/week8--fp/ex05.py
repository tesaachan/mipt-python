"""
На вход подаётся последовательность натуральных чисел длины n≤1000.
Посчитайте произведение пятых степеней чисел в последовательности.
"""

from functools import reduce

print(
    reduce(
        lambda n, m: n * m,
        map(
            lambda n: int(n)**5,
            input().split()
        )
    )
)
