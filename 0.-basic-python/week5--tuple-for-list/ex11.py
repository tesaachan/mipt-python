"""
Напишите программу, которая находит в массиве элемент,
самый близкий по величине к данному числу.
"""


n = int(input())
nums = list(map(int, input().split()))
given = int(input())

found = 3001
for i in range(n):
    if abs(given - nums[i]) < abs(given - found):
        found = nums[i]

print(found)
