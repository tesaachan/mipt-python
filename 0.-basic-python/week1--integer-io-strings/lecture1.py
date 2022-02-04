# lecture-1
# integer numbers, input/output, simple operations with strings


# 1. output and data types

print("Hello, world")
print(2 + 3)

print('2 + 3 =', 2 + 3)  # по умолчанию "запятая в print" = "пробел"
print('1', '2', '3', sep=' + ')  # sep устанавливает знак вместо запятой
print('= ', 1 + 2 + 3, '\n', sep='')

# 2. variables and arithmetic

print(11*6)
print(11**6)  # возведение в степень
print(11//6)  # деление нацело
print(11%6)  # остаток от деления

print((23 + 8) % 24)  # заснули в 23:00, 8 часов спим -> вставать в 7:00
print((7 - 8) % 24)  # что было за 8 часов до 7 утра

speed = 108
time = 12
dist = time * speed
print('distance:', dist, '\n')

# 3. operations with strings

phrase = 'Hasta la vista'
who = '"baby"'
print(phrase, ', ', who, sep='')

ans = 2 + 3
expr = '2 + 3 = '
print(expr + str(ans), '\n')  # func str(): num into string

# 4. input data
print('abc' * 3)

name = input()
print('Hello,', name)

a = int(input())
b = int('100' * 10)
print(a + b)

# 5. application tasks
# Задвча: Пусть есть два товара, первый из них стоит A рублей B копеек, а второй - C рублей D копеек.
# Сколько рублей и копеек стоят эти товары вместе.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
cost1 = a * 100 + b
cost2 = c * 100 + d
totalCost = cost1 + cost2
print(totalCost // 100, totalCost % 100)

# 6. application tasks
# Задача: вводится число N, необходимо отрезать от него K последних цифр.
# Например, при N = 123456 и K = 3 ответ должен быть 123.

n = int(input())
k = int(input())
print(n // 10**k)

# Округление в большую сторону:
print(11 // 6)  # 1
print((11 + 6 - 1) // 6)  # 2

print((a + b - 1) // b)
# или
print((a - 1) // b + 1)

# 7. how variables work

# C = A // B
# D = A % B

# C * B + D = A

# Если B < 0: D <= 0, D > B
# Если B > 0: D >= 0, D < B
