"""
Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""


nums = list(map(int, input().split()))

for i in range(0, len(nums), 2):
    num = nums.pop(i)
    nums.insert(i+1, num)

print(" ".join(map(str, nums)))
