from os import pipe
from threading import Thread
import time

def count(n):
	while n > 0:
		n -= 1
		if (n == 50_000_000):
			print('go c: ')
			c = input()

t0 = time.time()
count(100_000_000)
count(100_000_000)
print(time.time() - t0)

t0 = time.time()
th1 = Thread(target=count, args=(100_000_000,))
th2 = Thread(target=count, args=(100_000_000,))

th1.start(); th2.start()
th1.join(); th2.join()
print(time.time() - t0)