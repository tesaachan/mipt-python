# visokosnii god

n = int(input())

if n % 4 == 0 and (n % 400 == 0 or n % 100 != 0):
    print('YES')
else:
    print('NO')
