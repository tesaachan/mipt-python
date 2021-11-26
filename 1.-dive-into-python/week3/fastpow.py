def fastpow(a, p):
	print(a)
	if (p == 1):
		return a
	if (p % 2 == 1):
		return a * fastpow(a, p-1)
	return fastpow(a*a, p/2)

a = int(input())
p = int(input())

b = fastpow(a, p)
# b = pow(a, p)
print(b)
