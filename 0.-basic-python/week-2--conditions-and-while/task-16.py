# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).

a = int(input())
b = int(input())
c = int(input())

ans = 0

if a == b:
    ans += 1
if a == c:
    ans += 1
if b == c:
    ans += 1

if 0 < ans < 3:
    ans += 1

print(ans)
