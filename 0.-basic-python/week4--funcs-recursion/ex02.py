"""
Даны два действительных числа x и y. 
Проверьте, принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу). 
Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO. 
На рисунке сетка проведена с шагом 1.
"""


def IsPointInSquare(x, y):
    if (x <= 1 and y <= 1) and (x >= -1 and y >= -1):
        return True
    else:
        return False

x = float(input())
y = float(input())

if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
