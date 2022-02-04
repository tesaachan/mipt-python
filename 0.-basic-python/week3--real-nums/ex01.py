# Даны длины сторон треугольника. Вычислите площадь треугольника.

x = float(input())
y = float(input())
z = float(input())

# x, y, z = map(float, input().split())
p = 0.5*(x+y+z)
square = (p*(p-x)*(p-y)*(p-z))**0.5
if square % 1.0 == 0:
    print(int(square))
else:
    print('{:0.6f}'.format(square))
