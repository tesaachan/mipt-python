# Словари

from typing import Collection


empty_dict = {}
empty_dict = dict()

collections_map = {
	'mutable': ['list', 'set', 'dict'],
	'immutable': ['tuple', 'frozenset']
}

beatles_map = {
	'Paul': 'Bass',
	'John': 'Guitar',
	'George': 'Guitar',
}

# Добавить элемент:

beatles_map['Ringo'] = 'Drums'

beatles_map.update({
	'Ringo': 'Drums'
})

# Удаление элемента:

del beatles_map('John')

beatles_map.pop('Ringo')

# setdefault - 
# установить ключ-значение, если такой ключ еще не существует:

unknown_dict = {}
unknown_dict.setdefault('key', 'default')

# Итерации

for key in collections_map:
	print(key)

for key, value in collections_map.items():
	print('{} - {}'.format(key, value))

# Ключи хранятся в неупорядоченном порядке.
# В структуре OrderedDict ключи хранятся в том порядке, в котором были добавлены.
