"""
Даны пять действительных чисел: x, y, xc, yc, r.
Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r. 

Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
"""


def isPointInCircle(x, y, xc, yc, r):
    if (x-xc)**2 + (y-yc)**2 <= r**2:
        return True
    else:
        return False

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if isPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
