# the car get over N km for one day, that days the car needs to get over M km:

n = int(input())
m = int(input())

days = (m + n - 1) // n
print(days)
