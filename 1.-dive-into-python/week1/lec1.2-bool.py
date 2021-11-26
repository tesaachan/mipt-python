# Логический тип

x = 2
print(1 < x < 3)
print(bool(12))

# bool(x) == true, если x != 0

x = 12
y = False
print(x or y)	# x - true, дальше не проверяет, 
				# поэтому не преобразовывает, ответ - 12

# Задача
# Определить является ли год високосным.

# Решение
# Год яв. високосным, если он кратен 4, но не кратен 100, либо кратен 400:

year = 2017
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)

# Стандартное решение:
import calendar
print(calendar.isleap(year))
