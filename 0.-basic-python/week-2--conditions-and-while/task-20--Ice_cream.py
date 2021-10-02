# В кафе мороженое продают по три шарика и по пять шариков.
# Можно ли купить ровно k шариков мороженого?

k = int(input())

if k < 3:
    print('NO')
elif k % 3 == 0 or k % 5 == 0 or k % 3 == 2 or k % 5 == 3:
    print('YES')
elif k >= 6 and (k - 6) % 5 == 0:
    print('YES')
elif k >= 9 and (k - 9) % 5 == 0:
    print('YES')
elif k >= 12 and (k - 12) % 5 == 0:
    print('YES')
else:
    print('NO')
