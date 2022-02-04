"""
Штаб гражданской обороны Тридесятой области решил обновить план спасения на случай ядерной атаки.
Известно, что все n селений Тридесятой области находятся вдоль одной прямой дороги.
Вдоль дороги также расположены m бомбоубежищ, в которых жители селений могут укрыться на случай ядерной атаки.

Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
необходимо для каждого селения определить ближайшее к нему бомбоубежище.
"""


def key_dist(atup):
    return atup[1]


def fmt_data(n):
    gottenData = list(map(int, input().split()))
    new_list = list()
    for i in range(n):
        new_list.append((i+1, gottenData[i]))

    return sorted(new_list, key=key_dist)


n = int(input())
vils = fmt_data(n)

m = int(input())
points = fmt_data(m)

ans = list()

i, j = 0, 0
dist = 10e9+1
while i < len(vils) and j < len(points):
    if abs(vils[i][1] - points[j][1]) < dist:
        dist = abs(vils[i][1] - points[j][1])
        j += 1
        if j == len(points):
            ans.append((vils[i][0], points[j-1][0]))
            i, j = i+1, j-1
            if i < len(vils):
                dist = 10e9+1
    else:
        ans.append((vils[i][0], points[j-1][0]))
        i, j = i+1, j-1
        if i < len(vils):
            dist = 10e9+1

ans.sort()

for i in range(len(ans)):
    print(ans[i][1], end=' ')
