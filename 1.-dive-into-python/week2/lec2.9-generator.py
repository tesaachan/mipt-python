# Генераторы

# Простейший генератор - функция в yield.

def even_range(start, end):
	current = start
	while current < end:
		yield current
		current += 2

# yield -
# временный return. Возвращается значение, но функция не завершает работу.

for number in even_range(0, 10):
	print(number)

ranger = even_range(0, 4)

next(ranger) # 0
next(ranger) # 2
# ...
# next(ranger) - exec. StopIteration

# Очень важно бывает хранить состояние функции
# и возвращаться к нему раз за разом.
# Это также помогает оптимизировать работу с памятью.



# Генератор N-ого числа Фибоначчи:

def fibonacci(number):
	a = b = 1
	for _ in range(number):
		yield a
		a, b = b, a + b 



# Также генератор может получать значения (исп. в асинхрон.):

def accumulator():
	total = 0
	while True:
		value = yield total
		print('Got: {}'.format(value))

		if not value: break
		total += value

generator = accumulator()

next(generator)
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(3)))
