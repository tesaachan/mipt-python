"""
Дано натуральное число n>1. Проверьте, является ли оно простым.
Программа должна вывести слово YES, если число простое и NO, если число составное
"""


def isPrime(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 1

    return True


n = int(input())
if isPrime(n):
    print("YES")
else:
    print("NO")
