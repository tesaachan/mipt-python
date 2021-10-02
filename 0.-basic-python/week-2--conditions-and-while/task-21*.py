# Решить в целых числах уравнение: (ax+b) / (cx+d) = 0

a, b = int(input()), int(input())
c, d = int(input()), int(input())

if a != 0 and b % a == 0:
    x = -b // a
elif a == 0 and b == 0:
    x = 'INF'
else:
    x = 'NO'

if c != 0:
    if x == (-d // c) and d % c == 0:
        x = 'NO'
elif c == 0 and d == 0:
    x = 'NO'

print(x)
