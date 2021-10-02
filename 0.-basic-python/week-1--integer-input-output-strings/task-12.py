# Pie costs A rubles B pennies. How much N pies costs:

a = int(input())
b = int(input())
n = int(input())

sum = (a * 100 + b) * n
rubles = sum // 100
pennies = sum % 100

print(rubles, pennies)
