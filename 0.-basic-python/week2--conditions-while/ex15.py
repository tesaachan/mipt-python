# Дано три числа. Упорядочите их в порядке неубывания.
# Программа должна считывать три числа a,b,c,
# затем программа должна менять их значения так,
# чтобы стали выполнены условия a≤b≤c, и программа выводит тройку a,b,c.

a = int(input())
b = int(input())
c = int(input())

if a > b:
    tmp = a
    a = b
    b = tmp
if b > c:
    tmp = b
    b = c
    c = tmp
if a > b:
    tmp = a
    a = b
    b = tmp

print(a, b, c)
