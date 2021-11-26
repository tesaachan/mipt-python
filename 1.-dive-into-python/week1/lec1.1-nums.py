# Числовые типы

# int

num = 13
print(num)

num = -10
num = 100_000_000

print(type(num)) 
# <class 'int'>


# float

num = 13.4
num = -10.2
num = 100_000.000_001
print(num)

num = 1.5e2			# 1.5 умножить на 10 в степени 2


# Конвертация типов

num = 150.2
num = int(num)
print(num)			# 150
print(float(num))	# 150.0


# Комплексные числа

num = 14 + 1j
print(type(num))
print(num.real)
print(num.imag)


# Основные операции с числами

a = 1
b = 2.0
print(a + b)		# 3.0
print(b - a)		# 1.0
c = 10
d = 5
print(c / d)		# 2.0
print(4 * (c/d))	# 8.0
print(4 ** 2)		# 16
print(4.0 ** 2)		# 16.0
print(13 // 5)		# 2
print(13 % 5)		# 3


# Поменять значения местами

a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)


# Изменяемость и неизменяемость

x = y = 0		# вместо x, y = 0, 0
x += 1

print(x, y)

x = y = []		# пустой список - объект изменяемый
x.append(1)
x.append(2)

print(x,y)
