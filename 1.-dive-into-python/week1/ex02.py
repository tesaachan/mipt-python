import sys

digit_string = sys.argv[1]

sum = 0
for c in digit_string:
	sum += int(c)
print(sum)


"""
Решение:

import sys

print(sum([int(x) for x in sys.argv[1]]))

"""
