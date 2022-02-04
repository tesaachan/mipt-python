"""
В олимпиаде участвовало N человек.
Каждый получил определенное количество баллов, при этом оказалось, что у всех участников разное число баллов.
Упорядочите список участников олимпиады в порядке убывания набранных баллов.
"""


class Man:
    name = ""
    grade = 0


n = int(input())

mans = list()
for i in range(n):
    man = Man()
    man.name, grade = input().split()
    man.grade = int(grade)
    mans.append(man)

mans.sort(key=lambda n: n.grade, reverse=True)

for i in mans:
    print(i.name)
