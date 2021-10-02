# N minutes have passed after 0:00. That's time cloak shows:

n = int(input())

hours = (n // 60) % 24
minutes = n % 60

print(hours, minutes)
