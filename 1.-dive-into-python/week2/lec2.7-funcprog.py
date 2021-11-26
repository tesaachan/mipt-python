# Функциональное программирование


# Функции можно передавать в другие функции:

def caller(func, params):
	return func(*params)

def printer(name, origin):
	print('I\'m {} of {}'.format(name, origin))

caller(printer, ['Moana', 'Motuni'])


# Замыкания
# В функциях можно создавать другие функции:

def get_multiplier():
	def inner(a, b):
		return a * b
	return inner

multiplier = get_multiplier()
multiplier(10, 11)						# 110
print(multiplier.__name__)				# inner

def get_multiplier_by(number):
	def inner(a):
		return a * number
	return inner

multiplier_by_2 = get_multiplier_by(2)
multiplier_by_2(10) 					# 20


# map, filter, lambda

def squarify(a):
	return a ** 2

sqrlist = list(map(squarify, range(5)))
print(sqrlist)


def is_positive(a):
	return a > 0

poslist = list(filter(is_positive, range(-2, 3)))
print(poslist)


lambdlist = list(map(lambda x: x ** 2, range(5)))
print(lambdlist)


# Функция превращающая список чисел в список строк:

def num_to_str_list(nums):
	return list(map(lambda x: str(x), nums))

list2 = num_to_str_list(range(5))

print("{} {}".format(list(range(5)), list2))


# functools

# reduce

from functools import reduce

def multiply(a, b):
	return a * b

reduce(multiply, [1, 2, 3, 4, 5])		# 120
reduce(lambda x, y: x*y, range(1, 6))	# 120


# partial
# Позволяет подменятл определённые аргументы и модифицировать
# поведение функций.

from functools import partial

def greeter(person, greeting):
	return '{}, {}!'.format(greeting, person)

hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')

print(hier('brother'))
print(helloer('sir'))



# Списочные выражения

# Обычный вариант:

square_list = []
for number in range(10):
	square_list.append(number ** 2)
print(square_list)

# Списочные выражения:

square_list = [number ** 2 for number in range(10)]
print(square_list)

even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)

# для словарей:
square_map = {number: number ** 2 for number in range(5)}
print(square_map)


# zip
# позволяет склеить 2 итерабельных объекта:

num_list = range(7)
squared_list = [x ** 2 for x in num_list]

zip_list = list(zip(num_list, squared_list))
print(zip_list)


list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
))									# [(1, 1), (2, 2)]
