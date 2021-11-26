# Декораторы

# Декоратор -
# функция, которая принимает функцию и возвращает функцию.
# Чаще всего используются, чтобы модифицировать поведение каких-то функций.

def decorator(func):
	return func

@decorator
def decorated():
	print('Hello!')

# ^ происходит это:
decorated = decorator(decorated)


def decorator(func):
	def new_func():
		pass
	return new_func

@decorator
def decorated():
	print('Hello!')

print(decorated.__name__)			# new_func



# Декоратор, который записывает в лог результат
# декорируемой функции:

def logger(func):
	def wrapped(*args, **kwargs):
		result = func(*args, **kwargs)
		with open('log.txt', 'w') as f:
			f.write(str(result))
		return result
	return wrapped

@logger
def summator(num_list):
	return sum(num_list)

print("Summator: {}".format(summator([1, 2, 3, 4, 5])))		# 15

with open('log.txt', 'r') as f:
	print('log.txt: {}'.format(f.read()))



# Декоратор с параметром, который записывает лог в указанный файл.

def logger(filename):
	def decorator(func):
		def wrapped(*args, **kwargs):
			result = func(*args, **kwargs)
			with open(filename, 'w') as f:
				f.write(str(result))
			return result
		return wrapped
	return decorator


@logger('new_log.txt')
def summator(num_list):
	return sum(num_list)

summator([1,2,3,4,5,6])
# summator = logger('log.txt')(summator) то же самое

with open('new_log.txt', 'r') as f:
	print(f.read())



# Двойной+ декоратор

def first_decorator(func):
	def wrapped():
		print('Inside first_decorator')
		return func()
	return wrapped

def second_decorator(func):
	def wrapped():
		print('Inside second decorator')
		return func()
	return wrapped

@first_decorator
@second_decorator
def decorated():
	print('Finally called...')

# decorated = first_decorator(second_decorator(decorated))

decorated()

'''
Inside first_decorator
Inside second decorator
Finally called...
'''