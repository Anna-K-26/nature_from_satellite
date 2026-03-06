# spisok = []
# letters = []
# # value, l = 0, 'a'
# while True:
#     stroka = input()
#     if stroka == 'ФИНИШ':
#         break
#     stroka = stroka.lower()
#     spisok.append(stroka)
# for st in spisok:
#     for el in st:
#         letters.append(el)
#
# letters = [(letter, letters.count(letter)) for letter in letters]
# letters = sorted(letters, key=lambda item: item[1], reverse=True)
#numbers = [0, 4, 5, -9, -6, 3, 2, 3, 4, 9]

# x = input()
# if x == x[::-1]:
#     print(True)
# else:
#     print(False)

tup1 = (1, 2)
tup2 = (3, 4, 5)
# tup = []
# # index1 = 0
# # index2 = 0
# for i in range(len(tup1)):
#     for j in range(len(tup2)):
#         if tup1[i] > tup2[j]:
#             tup.append(tup2[j])
#         else:
#             tup.append(tup1[i])
# print(tuple(tup))
#
# numbers = [0, 4, 5, -9, -6, 3, 2, 3, 4, 9]
# spisok_spiskov = []
# spisok_spiskov.append([numbers[0]])
# i = 1
# while i < len(numbers):
#     if numbers[i] > numbers[i - 1]:
#         spisok_spiskov[0].append(numbers[i])
#     else:
#         spisok_spiskov.append([numbers[i]])
#     i += 1
# print(spisok_spiskov)

# def fibonacci(index):
#     a, b = 0, 1
#     spisok = []
#     if index == 1:
#         return 0
#     elif index == 2:
#         return 1
#     for _ in range(2, index + 1):
#         a, b = b, a + b
#         spisok.append(b)
#     for i, number in enumerate(spisok):
#         if i == len(spisok) - 1:
#             return number
# a = fibonacci(10)
# print(a)

# def fibonacci(index):
#     a, b = 0, 1
#     spisok = []
#     if index == 1:
#         return 0
#     for _ in range(2, index):
#         a, b = b, a + b
#         spisok.append(b)
#     for i, number in enumerate(spisok):
#         if i == len(spisok) - 1:
#             return number
# a = fibonacci(3)
# print(a)

# from sys import stdin
# for name in stdin:
#     with open(name, 'r') as file_name:
#         spisok = []
#         stroka = file_name.read()
#         words = stroka.split()
#         word_count = {}
#         for elem in words:
#             if elem in word_count:
#                 word_count[elem] += 1
#             else:
#                 word_count[elem] = 1
#         for key, value in word_count.items():
#             spisok.append((value, key))
#         spisok.sort(key=lambda x: (-x[0], not x[1][0].isupper(), x[1]))
#         for elem in spisok:
#             print('{} {}'.format(elem[0], elem[1]))


# def last_discharge(a):
#     if '.' in a:
#         spisok_a = a.split('.')
#         if spisok_a[0] == 0:
#             cel_chast = 0
#         else:
#             cel_chast = int(spisok_a[0])
#             drob_chast = spisok_a[1]
#             if drob_chast:
#                 last_razr = len(drob_chast.rstip('0')) - 1
#                 if last_razr < 0:
#                     new_drob_chast = 9 * len(drob_chast)
#                     if cel_chast > 0:
#                         return '{}.{}'.format(cel_chast - 1, new_drob_chast)
#                     else:
#                         return '{}.{}'.format(0, new_drob_chast)
#                 spisok = list(drob_chast)
#                 tecush_pozic = last_razr
#                 while tecush_pozic > 0:
#                     tecush_cifra = int(spisok[tecush_pozic])
#                     if tecush_cifra > 0:
#                         spisok[tecush_pozic] = str(tecush_cifra - 1)
#                         break
#                     else:
#                         spisok[tecush_pozic] = '9'
#                         tecush_pozic -= 1
#                     if tecush_pozic < 0:
#                         new_cel_chast = cel_chast - 1
#                         return '{}.{}'.format(new_cel_chast, ''.join(spisok))
#                     return '{}.{}'.format(cel_chast, ''.join(spisok))
#                 else:
#                     return str(cel_chast - 1)
#             else:
#                 return str(int(a) - 1)


