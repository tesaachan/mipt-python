"""
Дана строка, в которой буква h встречается минимум два раза.
Удалите из этой строки первое и последнее вхождение буквы h,
а также все символы, находящиеся между ними.
"""

str = input()
pos = first = last = str.find("h")
while (pos != -1):
    last = pos
    pos = str.find("h", pos+1)
str1 = str[:first]
str2 = str[last+1:]
print("{}{}".format(str1, str2))
