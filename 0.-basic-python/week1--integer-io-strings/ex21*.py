# check if four-digit number is symmetric: print 1 if true

# поделим число на две части (на два двузначных числа)
# второе число развернём цифрами
# прибавим к кажому числу число 2, чтобы исключить случай, когда исходное число будет 0
# если числа равны, то при делении одного нацело на другое будет 1, а остаток будет 0

n = int(input())

first_part = n // 100
second_part = n % 100

sf_part = second_part // 10
ss_part = second_part % 10
second_part = ss_part * 10 + sf_part

second_part = second_part + 2
first_part = first_part + 2

ans = first_part // second_part + first_part % second_part
print(ans)
