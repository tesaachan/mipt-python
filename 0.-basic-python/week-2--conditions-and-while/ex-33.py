# coding=utf-8
# Определите число всех элементов последовательности, завершающейся числом 0.

count = 0
n = int(input())
while n != 0:
    count += 1
    n = int(input())
print(count)
