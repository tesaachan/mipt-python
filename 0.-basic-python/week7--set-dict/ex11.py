"""
В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей.
Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.
"""


with open("input.txt", "r", encoding="utf-8") as file_from:
    names = file_from.readlines()
names[-1] += "\n"
all_votes = len(names)
candidates, winners = dict(), list()
for name in names:
    candidates[name] = candidates.get(name, 0) + 1
for name, num in candidates.items():
    winners.append((num, name))
winners.sort(reverse=True)
with open("output.txt", "w", encoding="utf-8") as file_to:
    if 2 * winners[0][0] > all_votes:
        print(winners[0][1][:-1], file=file_to)
    else:
        print(winners[0][1][:-1], file=file_to)
        print(winners[1][1][:-1], file=file_to)
