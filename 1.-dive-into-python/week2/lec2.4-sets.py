# Множества

empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}
# {1, 2, 3, 4, 5}

print(2 in number_set)	# True

# Добавление и удаление:

number_set.add(6)

number_set.remove(6)




odd_set = {1, 3, 5, 7, 9}
even_set = {2, 4, 6, 8}

# Объединение:

union_set = odd_set | even_set

union_set = odd_set.union(even_set)

# Пересечение:

intersection_set = odd_set | even_set

intersection_set = odd_set.intersection(even_set)

# Разность:

difference_set = odd_set - even_set
difference_set = odd_set,difference_set(even_set)



# frozenset -
# неизменяемое множество

frozen = frozenset(['Anna', 'Elza', 'Olaf'])
