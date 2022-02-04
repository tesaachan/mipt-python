"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
"""


with open("input.txt", 'r', encoding='utf8') as file:
    text = file.readlines()

words = list()
for line in text:
    words.extend(line.split())

repeats = dict()
for w in words:
    value = repeats.get(w, 0)
    print(value, end=' ')
    repeats[w] = value + 1
