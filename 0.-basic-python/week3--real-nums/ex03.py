# Дано положительное действительное число X. Выведите его дробную часть.

from math import floor
x = float(input())
print(x - floor(x))
