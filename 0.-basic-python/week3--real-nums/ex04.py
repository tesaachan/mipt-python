# Цена товара обозначена в рублях с точностью до копеек, то есть действительным числом с двумя цифрами после десятичной точки. 
# Запишите в две целочисленные переменные стоимость товара в виде целого числа рублей и целого числа копеек и выведите их на экран. 
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.

import math
x = float(input())

y = math.floor(x)
z = round((x - y)*100)
print("{} {}".format(y, z))
