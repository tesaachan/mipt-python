"""
В списке все элементы попарно различны.
Поменяйте местами минимальный и максимальный элемент этого списка.
"""


nums = list(map(int, input().split()))

max = (0, nums[0])
min = tuple(max)

for i in range(1, len(nums)):
    if nums[i] < min[1]:
        min = (i, nums[i])
    if nums[i] > max[1]:
        max = (i, nums[i])

nums[min[0]], nums[max[0]] = nums[max[0]], nums[min[0]]

print(" ".join(map(str, nums)))
