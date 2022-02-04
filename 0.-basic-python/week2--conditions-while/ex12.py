# На доске стоит белая шашка.
# Требуется определить, может ли она попасть в заданную клетку,
# делая ходы по правилам и не пользуясь ходами дамки.
# Белые шашки могут ходить по клеткам одного цвета по диагонали вверх-влево
# или вверх-вправо. Ходов может быть несколько!

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if ((x1 + y1) % 2 == (x2 + y2) % 2) and (y2 > x1) and (x2 + y2 >= x1 + y1):
    print('YES')
else:
    print('NO')