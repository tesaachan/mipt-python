# snail goes on height H,
# getting up A meters daily and getting down B meters at night
# how much days to H:

h = int(input())
a = int(input())
b = int(input())

# отнимем от H путь, который улитка преодолеет за последний день (без ночи)
# затем посчитаем сколько дней потребуетсяя улитке на то, чтобы пройти H-A за A-B км в день
# и округлим до большего целого по физическим причинам
h = h - a
days = 1

days = days + ((h + (a - b) - 1) // (a - b))
print(days)
