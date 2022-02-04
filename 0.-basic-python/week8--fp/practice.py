from functools import partial


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = sorted(
    [sorted(sub, reverse=True) for sub in a],
    reverse=True
    )


c = list(map(
    lambda n, m: list(map(
        lambda x, y: x + y, 
        n, m)), 
    a, b))

print(c)

# print(*filter(lambda n: n > 0, map(int, input().split())))
def funnc(a, b):
    return a + b

funncX = partial(funnc, b=5)
print(funncX(3))
