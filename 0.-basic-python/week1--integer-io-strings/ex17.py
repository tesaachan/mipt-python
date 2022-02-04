# cloak from seconds to h:mm:ss

n = int(input())

h = (n // 3600) % 24
m = (n - (n // 3600) * 3600) // 60
s = n - (n // 3600) * 3600 - m * 60

print(h, f'{m:02d}', f'{s:02d}', sep=':')
