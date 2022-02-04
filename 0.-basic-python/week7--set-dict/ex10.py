"""
Дан текст.
Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.
"""


import sys

repeats, words = dict(), list()
for line in sys.stdin.readlines():
    for word in line.split():
        repeats[word] = repeats.get(word, 0) + 1
for word, num in repeats.items():
    words.append((-num, word))
words.sort()
for w in words:
    print(w[1])
