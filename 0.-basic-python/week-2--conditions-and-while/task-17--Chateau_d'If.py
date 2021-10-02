# За многие годы заточения узник замка Иф проделал в стене
# прямоугольное отверстие размером D×E.
# Замок Иф сложен из кирпичей, размером A×B×C.
# Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие
# (очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())

min = a * b
side1 = a
side2 = b

if a * c < min:
    min = a * c
    side2 = c
if b * c < min:
    min = b * c
    side1 = b
    side2 = c

if d >= side1 and e >= side2:
    print('YES')
elif d >= side2 and e >= side1:
    print('YES')
else:
    print('NO')
