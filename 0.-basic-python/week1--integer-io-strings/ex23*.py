# check if A can be divided by B: YES if true, NO if false

a = int(input())
b = int(input())

x = a % b == 0

print("YES"*x + "NO"*(1-x))
