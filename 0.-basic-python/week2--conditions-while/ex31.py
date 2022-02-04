# Последовательность состоит из целых чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

n = int(input())
maxNum = n

while n != 0:
    n = int(input())
    if n != 0 and n > maxNum:
        maxNum = n

print(maxNum)
