# coding=utf-8
# Вывести второй максимум

n = int(input())
max2 = 0
max1 = n
while n != 0:
    n = int(input())
    if n < max1:
        if n > max2:
            max2 = n
    else:
        max2 = max1
        max1 = n
print(max2)
