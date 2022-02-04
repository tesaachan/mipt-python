"""
Каждый из N школьников некоторой школы знает Mᵢ языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
"""


students = list()

for i in range(int(input())):
    langs = set()
    for j in range(int(input())):
        lang = input()
        langs.add(lang)
    students.append(langs)

all = set(students[0])
at_least_one = set()
for i in students:
    all &= i
    at_least_one |= i
print(len(all), "\n".join(all), sep='\n')
print(len(at_least_one), "\n".join(at_least_one), sep='\n')
