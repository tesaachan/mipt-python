# lecture 2
# conditions and while cycle

# 1. Boolean data type and operations

# принимает True или False: == != < > <= >=
# приоритеты их одниаковы и меньше, чем арифметическе операции

# Операции and, or, not имеют приоритет ниже, чем у сравнений
# однако их приоритет разный: not > and > or

# 2. Examples

n = 9
is_even = n % 2 == 0
print(is_even)

# входит ли один отрезок в другой:

start1 = int(input())
finish1 = int(input())
start2 = int(input())
finish2 = int(input())

is_s1_in_2 = start1 <= start1 <= finish1
is_f1_in_2 = start2 <= finish1 <= finish2
is_s2_in_1 = start1 <= start2 <= finish1
is_f2_in_1 = start1 <= finish2 <= finish1

answer = is_s1_in_2 or is_f1_in_2 or is_s2_in_1 or is_f2_in_1
print(answer)

# то же самое что и

answer = start1 <= finish2 and start2 <= finish1
print(answer)

# 3. Conditions

x = int(input())
if x < 0:
    x = -x
print(x)

x = int(input())
if x >= 0:
    print(x)
else:
    print(-x)

x = abs(x)

y = True or 42 // 0 == 5 # не вызовет ошибки деления на 0,
# так как если первое условие выполнилось, то второе даже не будет проверяться

# 4. Inserted condition and elif

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('I')
    else:
        print('IV')
else:
    if y > 0:
        print('II')
    else:
        print('III')

if x == 1:
    print('One')
elif x == 2:
    print('Two')
elif x == 3:
    print('Three')
else:
    print('Other')
