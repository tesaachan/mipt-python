"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
Программа должна быть эффективной и не выполнять лишних действий!
"""

nums = list(map(int, input().split()))

for i in range(0, len(nums), 2):
    print(nums[i], end=' ')
