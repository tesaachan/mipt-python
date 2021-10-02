# Даны три целых числа A, B, C.
# Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

a = int(input()) % 2
b = int(input()) % 2
c = int(input()) % 2

if (a != b) or (a != c) or (c != b):
    print('YES')
else:
    print('NO')
