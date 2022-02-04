"""
Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
"""

str = input()

words = 0
pos = 0
while pos != -1:
    pos = str.find(" ", pos+1)
    words += 1

print(words)
