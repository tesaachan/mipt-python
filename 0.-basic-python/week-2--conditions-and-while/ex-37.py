# coding=utf-8
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

n = int(input())
temp = n
max_count = 1
count = 1
while n != 0:
    n = int(input())
    if n == temp:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1
    temp = n
print(max_count)
