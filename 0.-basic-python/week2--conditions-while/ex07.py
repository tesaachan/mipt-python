# Даны 2 клетки шахматной доски (координаты (x;y))
# Если они одного цвета - YES, если разных - NO:

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())


if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
    print("YES")
elif (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
    print("YES")
else:
    print("NO")
