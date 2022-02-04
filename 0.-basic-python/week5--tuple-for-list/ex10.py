"""
Выведите значение наименьшего из всех положительных элементов в списке.
Известно, что в списке есть хотя бы один положительный элемент, а значения всех элементов списка по модулю не превосходят 1000.
"""


nums = list(map(int, input().split()))

min_positive = 1001
for i in nums:
    if i > 0 and i < min_positive:
        min_positive = i

print(min_positive)
