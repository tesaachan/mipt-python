# coding=utf-8
# Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

n = int(input())
max = n
count = 1
while n != 0:
    n = int(input())
    if n > max:
        max = n
        count = 1
    elif n == max:
        count += 1
print(count)
