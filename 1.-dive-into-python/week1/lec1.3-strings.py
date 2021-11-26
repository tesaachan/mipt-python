# Строковые типы

from typing import Sequence


example_string = "Курс по Python на \"Coursera\" - " \
					"хороший курс"
print(example_string)

print(id(example_string))	# ячейка памяти по id()
example_string += " tre"
print(id(example_string))	# другая уже ячейка

# Срезы строк

example_string = "Курс по Python на \"Coursera\""
print(example_string[:5])
print(example_string[8:])
print(example_string[-9:])

print(example_string.count('P'))	# count() - количество символов
str = "moscow"
print(str.capitalize())				# Moscow
print("2017".isdigit())				# True

"3.14" in "Pi = 3.1415926"			# True

for letter in str.capitalize():
	print(letter)


# Форматирование строк

str = "{} знает тебя хорошо, но {} знает лучше.."
print(str.format("Твой муж", "твой босс"))

str = "{first} знает тебя хорошо, но {second} знает лучше.."
print(str.format(first="Твой муж", second="твой босс"))

# самый удобный способ:

first = "Твой муж"
second = "твой босс"
str = f"{first} знает тебя хорошо, но {second} знает лучше.."
print(str)

# цифры

num = 2/3
print(num)
print(f"{num:.3f}")				# 3 цифры после точки


# Байтовые строки

example_bytes = b"hello"
for element in example_bytes:
	print(element)

example_string = "привет"
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
decoded_string = encoded_string.decode()
print(decoded_string)
