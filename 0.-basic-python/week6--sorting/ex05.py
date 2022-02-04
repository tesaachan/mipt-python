"""
Известно, что фамилии всех участников — различны.
Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке.
При выводе указываете фамилию, имя участника и его балл.

Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').
"""


file_from = open('input.txt', 'r', encoding='utf-8')
file_to = open('output.txt', 'w', encoding='utf-8')

file_lines = file_from.readlines()
file_lines.sort()

fmt_lines = list()
for line in file_lines:
    fmt_lines.append(list(line.split()))

for line in fmt_lines:
    print(line[0], line[1], line[3], file=file_to)

file_from.close()
file_to.close()
