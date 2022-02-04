"""
Дан текст.
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""


import sys

text = sys.stdin.readlines()
max_num = 0
words, repeats = list(), dict()
for line in text:
    for w in line.split():
        repeats[w] = repeats.get(w, 0) + 1
        if repeats[w] > max_num:
            max_num = repeats[w]

max_words = list()
for word, num in repeats.items():
    if num == max_num:
        max_words.append(word)
max_words.sort()
print(max_words[0])
