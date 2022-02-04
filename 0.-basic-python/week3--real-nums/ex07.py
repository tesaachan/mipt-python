# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.

a = float(input())
b = float(input())
c = float(input())

D = b*b - 4*a*c
if D > 0:
    x1 = (-b - D**0.5)/(2*a)
    x2 = (-b + D**0.5)/(2*a)

    if x2 > x1:
        print("{:0.6f} {:0.6f}".format(x1, x2))
    else:
        print("{:0.6f} {:0.6f}".format(x2, x1))
elif D == 0:
    x = (-b)/(2*a)
    print(x)
