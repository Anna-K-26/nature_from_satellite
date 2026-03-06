spisok = []
letters = []
counts = []

# value, l = 0, 'a'
# while True:
#     stroka = input()
#     if stroka == 'ФИНИШ':
#         break
#     spisok.append(stroka)
#
# for row in spisok:
#     for letter in row.strip():
#         letter = letter.lower()
#         try:
#             index = letters.index(letter)
#             counts[index] += 1
#         except ValueError:
#             letters.append(letter)
#             counts.append(1)
#
# print(letters)
# print(counts)
#
# result = sorted(zip(letters, counts), key=lambda item: item[1])
# max_count = result[-1][1]
# letters = [letter for letter, count in result if count == max_count]
# letters = sorted(letters)
# print(letters[0])

spisok = []
Spisok = []
names = []
toys = []
Sp = []
N = int(input())
for _ in range(N):
    s = input()
    spisok.append(s)
for el in spisok:
    el = el.split()
    names.append(el[0].replace(':', ''))
    for i in range(1, len(el)):
        el[i] = el[i].replace(',', '')
        toys.append(el[i])
toys = set(toys)
spisok_keys = list(toys)
spisok_values = []
for element in names:
    if
d = dict(zip(spisok_keys, spisok_values))
print(names)
print(toys)
#     names.append(el[0].replace(':', ''))
#     toys.append(el[1:].replace(',', ''))
# print(toys)
# print(names)