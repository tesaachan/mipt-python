"""
Даны два целочисленных списка A и B, упорядоченных по неубыванию.
Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
Решение оформите в виде функции merge(A, B), возвращающей новый список.
Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.
"""


def merge(alist, blist):
    res = list()
    i, j = 0, 0
    while i < len(alist) and j < len(blist):
        if alist[i] <= blist[j]:
            res.append(alist[i])
            i += 1
        else:
            res.append(blist[j])
            j += 1

    res.extend(alist[i:])
    res.extend(blist[j:])
    return res

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums3 = merge(nums1, nums2)
for n in nums3:
    print(n, end=' ')
