"""
Дан список чисел.
Выведите все элементы списка, которые больше предыдущего элемента.
"""


nums = list(map(int, input().split()))

prev = nums[0]
for i in nums:
    if i > prev:
        print(i, end=' ')
    prev = i
