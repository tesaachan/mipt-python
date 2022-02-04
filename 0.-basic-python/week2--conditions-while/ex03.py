# nums a, b, c. What is the biggest one:

a = int(input())
b = int(input())
c = int(input())

if b > a:
    a = b
if c > a:
    a = c
print(a)
