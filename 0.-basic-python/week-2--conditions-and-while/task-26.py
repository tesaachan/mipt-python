# Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель, отличный от 1.

n = int(input())

min = n
i = 2
while i < n:
    if (n // i == n / i) and i < min:
        min = i
    i = i + 1

print(min)
