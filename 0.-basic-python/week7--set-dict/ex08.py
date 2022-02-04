"""
Программа получает на вход количество пар синонимов N.
Далее следует N строк, каждая строка содержит ровно два слова-синонима.
После этого следует одно слово.
"""


n = int(input())

syns = dict()
for i in range(n):
    word_1, word_2 = input().split()
    syns[word_1] = word_2
    syns[word_2] = word_1

word = input()
print(syns[word])
