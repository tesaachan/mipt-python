# Функции

# Аннотация функции:

def add(x: int, y: int) -> int:
	return x + y

# Однако это только аннотация!

# Все объекты передаются по ссылке!
# Однако изменение объекта является плохим тоном (как и везде),
# лучше пользоваться return.

# Именованные аргументы

def say(greeting, name):
	print('{}, {}!'.format(greeting, name))

say("Hello", "Kate")
say(name="Max", greeting="Hi")



# Из функции нельзя изменять объекты не из её области видимости:



# Аргументы по умолчанию

def greeting(name="it's me..."):
	print('Hello, {}'.format(name))

greeting()

def append_one(iterable=[]):
	iterable.append(1)

	return iterable

# Важно:

print(append_one())		# [1]
print(append_one())		# [1, 1]
# так происходит потому что список - изменяемый объект и связь между 
# аргументом по умолчанию и функцией единственна и определена изначально.
# Так происходит со всеми изменяемыми значениями.

# В таком случае нужно передавать deafult значение как None:

def function(iterable=None):
	if iterable is None:
		iterable = []
	
def function(iterable=None):
	iterable = iterable or []


# Звездочки

def printer(*args):
	print(type(args))	# кортеж

	for arg in args:
		print(arg)
