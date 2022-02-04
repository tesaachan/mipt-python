"""
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ,
каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты,
набравшие менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают.
Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.

В конкурсе участвует N человек, при этом количество мест равно K.
Определите проходной балл, то есть такое количество баллов, что количество участников,
набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов,
набравших наибольшее количество баллов среди непринятых абитуриентов, общее число принятых абитуриентов станет больше K.

Программа должна вывести проходной балл в конкурсе.
Выведенное значение должно быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
Также возможны две ситуации, когда проходной балл не определен.
Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.
Если количество имеющих равный максимальный балл абитуриентов больше чем K, программа должна вывести число 1.
"""


file_from = open('input.txt', 'r', encoding='utf8')
file_to = open('output.txt', 'w', encoding='utf8')

data = file_from.readlines()
k = int(data[0])
grades = list()
for line in data[1:]:
    line = list(map(int, line.split()[-3:]))
    if list(map(lambda n: n >= 40, line)).count(True) == 3:
        grades.append(line[-3] + line[-2] + line[-1])

grades.sort(reverse=True)

if len(grades) <= k:
    ans = 0
else:
    while k >= 0 and grades[k-1] == grades[k]:
        k -= 1
    ans = grades[k-1]
    if k == 0 or k == -1:
        ans = 1

print(ans, file=file_to)
file_from.close()
file_to.close()