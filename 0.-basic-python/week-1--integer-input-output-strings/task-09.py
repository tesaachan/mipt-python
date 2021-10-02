# three-digit number, what's sum of its digits

n = int(input())

sum = n % 10 + (n // 10) % 10 + (n // 100)
print(sum)
