# По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).

n = int(input())

sum = 0
while n:
    sum += 1/(n**2)
    n -= 1

print("{:0.5f}".format(sum))
