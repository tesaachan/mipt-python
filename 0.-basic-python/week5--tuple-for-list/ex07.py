"""
Найдите количество положительных элементов в данном списке.
"""


nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num > 0:
        cnt += 1

print(cnt)
