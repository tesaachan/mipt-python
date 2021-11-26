# Списки (Lists)

empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
	['Elena', 4.4],
	['Andrey', 4.2]
]

len(collections)		# 4

print(collections[0])	# list

print(collections[-1])	# set

collections[3] = 'frozenset'

'tuple' in collections	# True

range_list = list(range(10))
print(range_list)

print(range_list[1:3])

print(range_list[::2])	# только чётные

print(range_list[::-1])	# в обратном порядке

for collection in collections:
	print('Learning {}...'.format(collection))

for idx, collection in enumerate(collections):
	print('#{} {}'.format(idx, collection))


# Добавление и удаление элементов

collections.append('OrderedDict')
print(collections)


# вставить список в список:

collections.extend(['ponyset', 'unicorndict'])
print(collections)

collections += [None]

# удаление:

del collections[4]

print(collections)


# Встроенные функции:

numbers = [4, 17, 19, 9, 2, 6, 10, 13]

min(numbers)
max(numbers)
sum(numbers)

tag_list = ['python', 'course', 'coursera']
print(', '.join(tag_list))


# Сортировка:

import random

numbers = []
for _ in range(10):
	numbers.append(random.randint(1, 20))

sorted(numbers)	# новый список
numbers.sort()	# отсортировать данный список

sorted(numbers, reverse=True)
numbers.sort(reverse=True)



# Множество популярных методов списков:

"""
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
"""

