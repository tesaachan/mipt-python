"""
Отсортируйте данный массив, используя встроенную сортировку.
"""

n = int(input())
nums = list(map(int, input().split()))

print(" ".join(map(str, sorted(nums))))
