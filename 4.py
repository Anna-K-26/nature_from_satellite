# import re
#
#
# s = input()
# s = re.split('[ ]', s)
# s_ = []
# for elem in s:
#     if elem not in ['+', '-', '*']:
#         s_.append(int(elem))
#     else:
#         print(s_)
#         a, b = s_[-2], s_[-1]
#         if elem == '+':
#             res = a + b
#         elif elem == '-':
#             res = a - b
#         else:
#             res = a * b
#         del s_[-1]
#         del s_[-1]
# #         s_.append(res)
# translit_dict = {
#     # Заглавные буквы (уже с правильным регистром первой буквы)
#     'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
#     'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
#     'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
#     'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
#     'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia',
#
#     # Строчные буквы
#     'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
#     'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
#     'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
#     'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
#     'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
# }
# s = input()
# spisok = []
# for el in s:
#     for keys, value in translit_dict.items():
#         if el == keys:
#             el = value
#     spisok.append(el)
# new_spisok = list(filter(lambda x: x != 'ь' and x != 'ъ' and x != 'Ь' and x != 'Ъ', spisok))
# print(new_spisok





