# Даны три стороны треугольника a,b,c.
# Определите тип треугольника с заданными сторонами.
# Выведите одно из четырех слов: rectangular для прямоугольного треугольника,
# acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника или
# impossible, если треугольника с такими сторонами не существует
# (считаем, что вырожденный треугольник тоже невозможен).

a = int(input())
b = int(input())
c = int(input())

big = a
lil1 = b
lil2 = c
if b > big:
    big = b
    lil1 = a
if c > big:
    big = c
    lil1 = a
    lil2 = b

if (big + lil1 > lil2) and (big + lil2 > lil1) and (lil1 + lil2 > big):
    if big**2 == lil1**2 + lil2**2:
        print('rectangular')
    elif big**2 > lil1**2 + lil2**2:
        print('obtuse')
    elif big**2 < lil1**2 + lil2**2:
        print('acute')
else:
    print('impossible')
