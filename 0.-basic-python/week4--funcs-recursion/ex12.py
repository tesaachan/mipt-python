"""
Ханойские башни
"""


def move(n, x, y):
    if n == 0:
        return
    z = 6 - x - y   # 3-й диск
    move(n-1, x, z)
    print(n, x, y)
    move(n-1, z, y)


n = int(input())
move(n, 1, 3)
