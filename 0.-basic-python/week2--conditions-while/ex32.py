# coding=utf-8
# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².

n = int(input())

sum = 0
while n > 0:
    sum = sum + n*n
    n = n - 1
print(sum)
