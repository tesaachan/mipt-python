# Объект None

# Аналог нулевому указателю из C

answer = None
print(type(answer))

bool(None)		# False

income = 0
if not income:
	print("Ничего не заработали")


income = None

if income is None:
	print("Еще не начали продавать")
elif not income:
	print("Ничего не заработали")


# Управление потоком

company = "google.com"
if "my" in company:
	print("ok")
elif "google" in company:
	print("also ok")
else:
	print("no")


score_1 = 5
score_2 = 0
winner = "Argentina" if score_1 > score_2 else "Jamaica"
print(winner)


for i in range(3):
	print(i)			# без 3

result = 0
for i in range(101):
	result += i
print(result)

for i in range(5, 8):
	print(i)
# 5 6 7

for i in range(1, 10, 2):
	print(i)
# 1 3 5 7 9

for i in range(10, 5, -1):
	print(i)
# 10 9 8 7 6

for i in range(100):
	pass
# pass - ничего не делать, заглушка

result = 0
while True:
	result += 1
	if result >= 100:
		break
print(result)		# 100

result = 0
for i in range(10):
	if i % 2 != 0:
		continue
	result += i
print(result)	# сумма четных чисел


# Random

import random
number = random.randint(0, 101)

str = "привет"
str = str[::-1]
print(str)			#тевирп