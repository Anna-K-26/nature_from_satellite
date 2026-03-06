from unicodedata import category

#a = input("Как Вас зовут?\n")
#print(f"Привет, {a}")

#Задача C
#a=int(input("Введите число: "))
#print(a)
#print(a)
#print(a)


#Задача D
#a=95
#b=int(input("Введите число: "))
#print(b-a)

#Задача E
#a=int(input("Цена товара за единицу веса: "))
#b=int(input("Вес товара: "))
#c=int(input("Количество денег у покупателя: "))
#print(c-a*b)

#Задача F
#name=input('Введите название: ')
#a=int(input('Цена товара за килограмм: '))
#b=int(input('Вес товара: '))
#c=int(input('Количество денег у пользователя: '))
#print('Чек')
#print(name, '-', b, '-', a, 'руб/кг')
#print('Сдача: ', c-a*b)

#Задача G (уточнить про новую строку)
#N=int(input('Введите число: '))
#stroka='Купи слона!'
#print(stroka*N)

#Задача H (вопрос!!!)
#N=int(input('Введите число: '))
#s=input('Введите строку: ')
#print(('Я никогда не буду писать s!')*N)
#print(s)

#Задача I
#N=int(input('Количество детей: '))
#M=int(input('Количество минут: '))
#n=2
#k=2
#t=2
# число кусков, которое съедает 1 человек за время t:
#v=k/n
# один человек за время M:
#result=(M/t*v)*N
#print(f"{result:.0f}")

#Задача J (идею подглядела) (уточнить про отступы и строки)
#name=(input("Введите имя: "))
#sh=(input("Введите номер шкафчика: "))
#print('Группа №{}.'.format(sh[0]))
#print('{}. {}.'.format(sh[2], name))
#print('Шкафчик: {}.'.format(sh))
#print('Кроватка: {}.'.format(sh[1]))

#Задача K

#s=input('Введите число: ')
#print(s[1]+s[0]+s[3]+s[2])


# Задача L (не получилась)



# Задача M
#N=int(input("Количество детей на утренике: "))
#M=int(input("Количество конфет в отсеке: "))
#print(M//N, M%N)

# Задача N
#a=int(input("Количество красных шариков: "))
#b=int(input("Количество зеленых шариков: "))
#c=int(input("Количество синих шариков: "))
#print(a+c+1)

# Задача O (Уточнить: как получить 0 перед 9 и 5?)

#N=int(input("Часов: "))
#M=int(input("Минут: "))
#T=int(input("Привезут через: "))
#summa_minut=N*60+M+T
#print(summa_minut//60,':', summa_minut%60)

# Задача P

#A=int(input("Склад: "))
#B=int(input("Магазин: "))
#C=int(input("Скорость: "))
#print(f"{(B-A)/C:.2f}")

# Задача Q
#a=int(input("Сумма купленных товаров на данный момент: "))
#b=(input("Сумма за последнюю покупку: "))
#print(a+int(b,2))

# Задача R
#a=(input("Сумма купленных товаров на данный момент: "))
#b=int(input("Сумма за последнюю покупку: "))
#print(b-int(a,2))

# Задача S
#s1 = '================Чек================'
#s2 = s3 = s4 = s5 = s6 = '' * 35
#s7 = '==================================='
#product = input()
#weight = input()
#price = input()
#kol_den = (input())
#s2[0:len('Товар:')] = 'Товар:'
#s3[0:len('Цена:')] = 'Цена:'
#s4[0:len('Итого:')] = 'Итого:'
#s5[0:len('Внесено:')] = 'Внесено:'
#s6[0:len('Сдача:')] = 'Сдача:'
#s2[len(s2) - len(product):len(s2)] = product
#_s3 = '{}кг * {}руб/кг'.format(price, weight)
#s3[len(s3) - len(_s3):len(s3)] = _s3
#_s4 = '{}руб'.format(int(weight) * int(price))
#s4[len(s4) - len(_s4):len(s4)] = _s4
#_s5 = '{}руб'.format(kol_den)
#s5[len(s5) - len(_s5):len(s5)] = _s5
#_s6 = '{}руб'.format(int(kol_den) - int(price) * int(weight))
#s6[len(s6) - len(_s6):len(s6)] = _s6
#print(s1)
#print(s2)
#print(s3)
#print(s4)
#print(s5)
#print(s6)
#print(s7)



# Задача T
#N=int(input("Общий вес котлет: "))
#M=int(input("Общий ценник за кг: "))
#K1=int(input("Стоимость 1-го вида котлет за кг: "))
#K2=int(input("Стоимость 2-го вида котлет за кг: "))

#Имеем систему уравнений:
#x+y=N
#x*K1+y*K2=M

#print(N*(M-K2)//(K1-K2), N*(K1-M)//(K1-K2))

# Задача А (подглядела)

#print("Как Вас зовут? ")
#name=input()
#print('Здравствуйте, {name}!')
#print("Как дела?")
#s=input()
#   print('Я за вас рада!')
#elif s=='плохо':
 #   print('Все наладится')

#Задача B

#P=int(input("Средняя скорость Пети: "))
#V=int(input("Средняя скорость Васи: "))

#if P>V:
#    print("Петя")
#else:
 #   print("Вася")

 #Задача C

#P=int(input("Средняя скорость Пети: "))
#V=int(input("Средняя скорость Васи: "))
#T=int(input("Средняя скорость Толи: "))

#if P>V and P>T:
 #   print("Петя")
#elif V>P and V>T:
  # print("Вася")
#elif T>P and T>V:
 #   print("Толя")

 #Задача D (сомневаюсь в правильности)
#P=int(input("Средняя скорость Пети: "))
#V=int(input("Средняя скорость Васи: "))
#T=int(input("Средняя скорость Толи: "))

#if P>V and V>T:
 #   print("1.Петя")
  #  print("2.Вася")
   # print("3.Толя")


#elif V>P and P>T:
 #   print("1.Вася")
  #  print("2.Петя")
   # print("3.Толя")

#elif T>P and P>V:
 #   print("1.Толя")
  #  print("2.Петя")
   # print("3.Вася")


#elif P>T and T>V:
 #   print("1.Петя")
  #  print("2.Толя")
   # print("3.Вася")

#elif V>T and T>P:
 #   print("1.Вася")
  #  print("2.Толя")
   # print("3.Петя")

#elif T>P and V>P:
 #   print("1.Толя")
  #  print("2.Вася")
   # print("3.Петя")


# Задача E
#N=int(input("Столько яблок дал Дима Пете: "))
#M=int(input("Столько яблок дал Дима Васе:"))

#start_P=6
#start_V=12

#if (N+start_P)>(M+start_V):
 #   print("Петя")
#else:
   # print("Вася")

#Задача F (не получилась)

#Задача G

#a=(input("Введите число: "))
#if a[0]==a[3] and a[1]==a[2]:
 #   print('YES')
#else:
 #   print('NO')

 # Задача H
#s=input("Введите строку: ")
#z='зайка'
#if z in s:
#    print('YES')
#else:
#     print('NO')

# Задача I
#s1=input("Введите первое имя: ")
#s2=input("Введите второе имя: ")
#s3=input("Введите третье имя: ")

#if s1[0] < s2[0] and s1[0] < s3[0]:
#    print(s1)
#elif s2[0] < s1[0] and s2[0] < s3[0]:
#    print(s2)
#elif s3[0] < s1[0] and s3[0] < s2[0]:
#    print(s3)

# Задача J

#s=input("Введите число: ")
#a=int(s[1]+s[2])
#b=int(s[0]+s[1])
#result=str(a+b)
#if a>b:
#    print(result[::-1])
#else:
#    print(result)

# Задача K (вопрос)

#s=(input("Введите число: "))
#for number in s:
#    print(max(number),min(number))
#a=max(number)
#b=min(number)

# (понимаю, что неправильно): c=s-str(a)-str(b)

#if a+b==2*int(c):
#    print('YES')

#else:
#    print('NO')

# Задача L
#a=int(input("Введите первое число: "))
#b=int(input("Введите второе число: "))
#c=int(input("Введите третье число: "))

#if (a + b) > c and (a+c) > b and (c+b) > a:
#    print('YES')
#else:
#    print('NO')

# Задача M
#s1 = input()
#s2 = input()
#s3 = input()
#len(s1) = len(s2) = len(s3)
#for i, a in enumerate(zip(s1, s2, s3)):
#    if s1[i] == s2[i] == s3[i]:
#        print(s1[i])

# Задача N

#s=input("Введите число: ")

#a=s[0]+s[1]
#b=s[0]+s[2]
#c=s[1]+s[2]

#if int(a[0]>a[1]):
#    result_a=a
#else:
#    result_a=(a[::-1])

#if int(b[0]>b[1]):
#    result_b=b
#else:
#    result_b=(b[::-1])

#if int(c[0]>c[1]):
#    result_c=c
#else:
#    result_c=(c[::-1])

#print(min(int(result_a),int(result_b),int(result_c)), max((int(result_a),int(result_b),int(result_c))))

# Задача N (новая версия)

#s = input()

#a = s[0] + s[1]
#b = s[0] + s[2]
#c = s[1] + s[2]

#a1 = s[1] + s[0]
#b1 = s[2] + s[0]
#c1 = s[2] + s[1]

#if a[0] == 0 or b[0] == 0 or c [0] == 0 or a1[0] == 0 or b1[0] == 0 or c1[0] == 0:
#    result_a = a[::-1]
#    result_b = b[::-1]
#    result_c = c[::-1]
 #   result_a1 = a1[::-1]
  #  result_b1 = b1[::-1]
   # result_c1 = c1[::-1]
#else:
#    result_a = a
#    result_b = b
#    result_c = c
#    result_a1 = a1
#    result_b1 = b1
#    result_c1 = c1

#print(min(int(result_a), int(result_b), int(result_c), int(result_a1), int(result_b1), int(result_c1)), max(int(result_a), int(result_b), int(result_c),  int(result_a1), int(result_b1), int(result_c1)))





# Задача O (не получилась)

#s1=input("Введите первое число: ")
#s2=input("Введите второе число: ")

#for number in s1,s2:
 #   a=max(number)
  #  c=min(number)
  #  if a==int(s1[0]) and c==int(s2[0]):
   #     b = int(s1[1])+int(s2[1])
   # elif a==int(s1[0]) and c==int(s2[1]):
   #     b = int(s1[1]) + int(s2[0])
   # elif a==int(s1[1]) and c==int(s2[0]):
   #     b = int(s1[0]) + int(s2[1])
   # elif a==int(s1[0]) and c==int(s1[0]) or  a==int(s1[1]) and c==int(s1[1]):
    #    b = int(s2[0]) + int(s2[1])
    #elif a == int(s2[0]) and c == int(s2[0]) or  a==int(s2[1]) and c==int(s2[1]):
     #   b = int(s1[0]) + int(s1[1])
      #  s=str(b)
       # if len(s)==1:
        #    print(str(a)+s[0]+str(b))
        #elif len(s)==2:
         #   print(str(a) + s[1] + str(b))

# Новая версия
# s1 = input()
# s2 = input()
#
# s1 = [int(digit) for digit in list(s1)]
# s2 = [int(digit) for digit in list(s2)]
#
# s = s1 + s2
#
# i_max, i_min = 0, 0
# a, b = s[0], s[0]
# for i, digit in enumerate(s):
#     if digit > a:
#         i_max = i
#         a = digit
#     if digit < b:
#         i_min = i
#         b = digit
#
# c = None
# d = None
# for i, digit in enumerate(s):
#     if i != i_max and i != i_min:
#         c = digit
#         _c = i
#         break
# for j,digit in enumerate(s):
#     if i != i_max and i != i_min and i != _c:
#        d = digit
#     break
#
# print(str(a) + str((c + d) % 10) + str(b))

# stroki = []
# for i in range(1, 4):
#     x = input()
#     stroki.append(x)
# wtf = 'зайка'
# stroki2 = []
# for s in stroki:
#     for i in range(0, len(s) - len(wtf)):
#         if s[i:i + len(wtf)] == wtf:
#             stroki2.append('{} {}'.format(s, len(s)))
#             break
# print(sorted(stroki2))

# stroki = []
# while True:
#     x = input()
#     if x == 'Приехали!':
#         break
#     stroki.append(x)
# k = 0
# wtf = 'зайка'
# for i in range(len(stroki)):
#     flag = False
#     if wtf in stroki[i]:
#         flag = True
#         break
#     if flag:
#         k += 1
# print(k)






# Задача P (пока что отложила)

# Задача Q (уточнить: почему не сошелся второй вывод?)

#a=float(input("Введите число 'a': "))
#b=float(input("Введите число 'b': "))
#c=float(input("Введите число 'c': "))

#if a!=0 and b**2-4*a*c<0 or a==0 and b==0 and c!=0:
 #   print('No solution')
#elif a!=0 and b**2-4*a*c>0:
 #   print(f"{(-b-(b**2-4*a*c)**0.5)//(2*a):.2f}", f"{(-b+(b**2-4*a*c)**0.5)//(2*a):.2f}")
#elif a!=0 and b**2-4*a*c==0:
 #   print(f"{(-b - (b ** 2 - 4 * a * c) ** 0.5) // (2 * a):.2f}")

#elif a==0 and b!=0 and c!=0:
  #  print(f"{-c/b:.2f}")
#elif a==0 and b==0 and c==0:
 #   print('Infinite solutions')

# Задача R

#a=float(input("Введите длину стороны 'a': "))
#b=float(input("Введите длину стороны 'b': "))
#c=float(input("Введите длину стороны 'c': "))

#if a**2+b**2==c**2 and a**2+c**2>b**2 and c**2+b**2>a**2:
 #   print('100%')
#elif a**2+c**2==b**2 and a**2+b**2>c**2 and c**2+b**2>a**2:
 #   print('100%')
#elif b**2+c**2==a**2 and a**2+b**2>c**2 and c**2+a**2>b**2:
 #   print('100%')

#elif a**2+b**2>c**2 and a**2+c**2>b**2 and c**2+b**2>a**2:
 #   print('мала')

#elif a**2+c**2<b**2 and a**2+b**2>c**2 and b**2+c**2>a**2:
    #print('велика')
#elif c**2+b**2<a**2 and a**2+b**2>c**2 and a**2+c**2>b**2:
 #   print('велика')
#elif a**2+b**2<c**2 and b**2+c**2>a**2 or c**2+a**2>b**2:
 #   print('велика')

# новая версия
#a = float(input())
#b = float(input())
#c = float(input())

#if a ** 2 + b ** 2 == c ** 2 or  a ** 2 + c ** 2 == b ** 2 or  c ** 2 + b ** 2 == a ** 2:
 #   print('100 %')
#elif a ** 2 + b ** 2 < c ** 2 or  a ** 2 + c ** 2 < b ** 2 or  c ** 2 + b ** 2 < a ** 2:
  #  print('велика')
#else:
 #   print('крайне мала')


# Задача S (не совсем поняла условие)
#a=float(input("Введите первое число: "))
#b=float(input("Введите второе число: "))

#   print('Опасность! Покиньте зону как можно скорее!')
#elif -10 <= a <= 10 and -10 <= b <= 10:
 #   print('Зона безопасна. Продолжайте работу.')

#else:
 #   print('Вы вышли в море и рискуете быть съеденным акулой!')

# Задача T (не получилась)
#s1=input('s1: ')
#s2=input('s2: ')
#s3=input('s3: ')

#z='зайка'

#if z in s1 and len(s1) == min(len(s1), len(s2), len(s3)):
#    print(s1, len(s1))
#elif z in s2 and len(s2) == min(len(s1), len(s2), len(s3)):
 #   print(s2, len(s2))
#elif z in s3 and len(s3) == min(len(s1), len(s2), len(s3)):
 #   print(s3, len(s3))

# Новая версия
#s1 = input()
#s2 = input()
#s3 = input()
#s = [s1, s2, s3]
#z = 'зайка'
#for i in range(3):
 #   if z in s[i] and s[i] == min(s[i]):
  #      print(z, len(s[i]))



# Задача A (циклы)
#kr=input('Введите слово: ')
#while kr!= 'Три!':
 #   print('Режим ожидания...')
  #  kr = input('Введите слово: ')

#print('Ёлочка, гори!')


# Задача B (не получилось)
#s=input('Введите строку: ')
#result=0
#while s!= 'Приехали!':
 #    result+= s

# Задача C
#n=int(input('Скажите начало диапазона: '))
#k=int(input('Скажите конец диапазона: '))

#for i in range(n,k+1):
 #   print(i)

# Задача E (вопрос: как ввести любое количество чисел?)

#numbers = []
#summa = 0
#while True:
 #  if a == 0:
  #      break
   # numbers.append(a)
#for a in numbers:
 #   if a >= 500:
  #      summa += a - a * 10 / 100
   # else:
    #    summa += a
#print(summa)

# Задача D
#a=int(input('Введите первое число: '))
#b=int(input('Введите второе число: '))

#if a<b:
 #   for i in range(a,b+1):
  #      print(i)
#elif a>b:
 #   for i in range(a,b-1,-1):
  #      print(i)

# Задача F
#a = int(input())
#b = int(input())

#r = a % b

#while r != 0:
 #   a, b = b, r
#print(r)

# Задача J
# Идею подглядела
#s = input()
#n = int(input())
#x, y = 0, 0
#while s != 'СТОП':
#    if s == 'СЕВЕР':
#        y += n
#    elif s == 'ЮГ':
#        y -= n
#    elif s == 'ВОСТОК':
#        x += n
 #   elif s == 'ЗАПАД':
  #      x -= n
#print(x)
#print(y)

# Задача K
#a = input()
#result = 0
#for i in range(len(a)):
#    result += int(a[i])
#print(result)

# Задача L
#a = input()
#l = []
#for i in range(len(a)):
#    l.append(int(a[i]))
#print(max(l))

# Задача M
#N = int(input())       # 1. Считываем число N
#spisok = []           # 2. Создаём пустой список

#for _ in range(N):     # 3. Цикл, повторяющийся N раз
 #   s = input()        # 4. Считываем строку с клавиатуры
  #  spisok.append(s)   # 5. Добавляем строку в список

#s_min = min(spisok)
#for s in spisok:
 #   if s == s_min:
  #      print(s)

# Задача N
#a = int(input())
#if a >= 2:
 ##         print('NO')
   #         break
    #    else:
     #       print('YES')
      #      break
#else:
 #   print('NO')

# Задача Q
#a = input()
#a = list(a)
#for i in range(len(a) -1, -1, -1):
 #   if int(a[i]) % 2 == 0:
  #      del a[i]
#print(''.join(a))

# Задача R
#a = int(input())
#spisok = []
#for i in range(2, int(a ** 0.5) + 1):
 #   if a % i == 0:
  #      for k in range(2, int(i ** 0.5) + 1):
   #         if i % k != 0 and i % 1 == 0 and i % i == 0:
    #            a = a // i
     #           spisok.append(i)
#for _ in range(len(spisok)):
 #   print(" * ".join(map(str, spisok)))

# Задача A
# n = int(input())
# result = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         result = i * j
#         print(result, end = '\t')

# Задача B
# n = int(input())
# for j in range(1, n + 1):
#     for i in range(1, n + 1):
#         print('{} * {} = {}'.format(i, j, i * j), end = '\t')

# Задача D
# N = int(input())
# spisok = []
# for _ in range(N):
#     n = input()
#     spisok.append(n)
# result = 0
# for s in spisok:
#     for i in range(len(s)):
#         result += int(s[i])
# print(result)

# Задача E
# N = int(input())
# spisok = []
# for _ in range(N):
#     while stroka != 'ВСЁ':
#         stroka = input()
#         spisok.append(stroka)
# z = 'зайка'
# spisok_z = []
# for s in spisok:
#     for i in range(len(s) - len(z) + 1):
#         if s[i:i + len(z)] == z:
#             spisok_z.append(z)
# print(len(spisok_z))

# Задача B
# max_number = int(input())
# row = 1
# col = 1
# number = 1
# spisok = []
# for i in range(1, max_number + 1):
#     spisok.append(i)

# a = int(input())
# b = int(input())
# c = a
# d = b
# while b != 0:
#         a_old = a
#         b_old = b
#         a = b_old
#         b = a_old % b_old
# print(c * d // a)

# import random
#
# left, right = 1, 1000
# for _ in range(10):
#     guess = random.randint(left, right)
#     print(f'{guess} ?')
#     ans = input().lower()
#     if ans in ['больше', '+']:
#         left = guess + 1
#     elif ans in ['меньше', '-']:
#         right = guess - 1
#     elif 'угадал' in ans:
#         print('Число отгадано')
#         exit(0)
# print('Не получилось((((')

# Задача F
# import math
# N = int(input())
# spisok = []
# nod = 1
# for _ in range(N):
#     a = int(input())
#     spisok.append(a)
# nod_0 = math.gcd(int(spisok[0]), int(spisok[1]))
# for i in range(len(spisok)):
#             nod = math.gcd(nod_0, spisok[i])
# print(nod)


# Задача G
# N = int(input())
# # for i in range(3, 0, -1):
# #     print('До старта осталось {} секунд(ы)'.format(i))
# # print('Старт 1!!!')
# for n in range(N):
#     for i in range(n + 3, 0, -1):
#         print('До старта осталось {} секунд(ы)'.format(i))
#     print('Старт {}!!!'.format(n + 1))

# Задача H
# N = int(input())
# spisok = []
# result = 0
# for _ in range(N):
#     name = input()
#     number = input()
#     spisok.append((name, number))
# # print(spisok[0][1][0])
# for i in range(len(spisok)):
#     for j in range(len(spisok[i])):
#         for k in range(len(spisok[i][j])):
#             result += int(spisok[i][j][k])
# print(max(result))

# Задача I
# N = int(input())
# spisok = []
# nums = []
# results = []
# for _ in range(N):
#     a = input()
#     spisok.append(a)
# # max_index, max_n = 0, -1
# for el in spisok:
#      for i in range(len(el)):
#          nums.append(int(el[i]))
#      max_value = max(nums)
#      results.append(max_value)
#      results = [str(n) for n in results]
# print(''.join(results))


# Задача J
# count = int(input())
# A = 'А'
# B = 'Б'
# C = 'В'
# print('{} {} {}'.format(A, B, C))
# for a in range(1, count):
#
#     #while a >= 1:
#      for b in range(1, count):
#
#         #while b >= 1:
#         for c in range(1, count):
#             while count - a - b >= 1:
#                 vov = count - a - b
#                    # while vov >= 1
#                    # while c >= 1
#                 print('{} {} {}'. format(a, b, vov))
#                 break
#             break


# А Б В
# 1 1 3
# 1 2 2
# 1 3 1
# 2 1 2
# 2 2 1
# 3 1 1

# Задача K
# N = int(input())
# spisok = []
# for _ in range(N):
#     a = int(input())
#     spisok.append(a)
# sp = []
# for el in spisok:
#     for i in range(2, int(el ** 0.5) + 1):
#         if el % i != 0:
#             sp.append(el)
# print(len(sp))


# Задача Q
# N = int(input())
# spisok = []
# for _ in range(N):
#     a = int(input())
#     spisok.append(a)
# spisok_new = list(map(str, spisok))
# sp = []
# for el in spisok_new:
#         if el == el[::-1]:
#             sp.append(el)
# print(len(sp))

# Задача L

# for number in range(1, M * N + 1):
#     for i in range(1, N):
#         while number <= N:
#             print('{}'.format(number), end=' ')
#             break
#         for j in range(1, M):
#             while number <= M:
#                  print('{}'.format(number), end=' ')
# Задача A (списки)
# N = int(input())
# spisok = []
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for el in spisok:
#     if el[0] != "а" and el[0] != "б" and el[0] != 'в':
#         print('NO')
#         break
#     else:
#         print('YES')
#         break

# Задача C
# L = int(input())
# N = int(input())
# spisok = []
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for el in spisok:
#     if len(el) > L:
#         print('{}...'.format(el[:L - 3]))
#     else:
#         print(el)

# Задача D
# spisok = []
# while True:
#     x = input()
#     if x == 'ВСЕ':
#         break
#     spisok.append(x)
#     # аналогично для случая цикла for s in spisok
# for i in range(len(spisok)):
#     if spisok[i][0] == '##':
#         del spisok[i][0]
#     print(' '.join(map(str, spisok)))
#     if spisok[i][len(spisok[i]) - 1] == '@@@':
#         del spisok[i][len(spisok[i]) - 1]
#     print(' '.join(map(str, spisok)))
# # print(' '.join(map(str, spisok)))

# Задача L
# N = int(input())
# M = int(input())
# i = 1
# k = 0
# s = ''
# for n in range(1, M * N + 1):
#     s += f'{n} '
#     k += 1
#     if k == M:
#         print(s)
#         i += 1
#         s = ''
#         k = 0
# print(s)

# Задача
# N = int(input())
# M = int(input())
# stroka = 1
# stolb = 1
# k = 0
# s = ''
# spisok = []
# spisok.append(s)
# for n in range(1, M * N + 1):
#     for el in spisok:
#         for j in range(len(el)):
#             for num in range(1, M + 1):
#                 spisok[j][num] = f'{n} '
#                 if num == N:
#                     stolb += 1
#                     k += 1
#                     if k == M:
#                         print(spisok[j][num])
#                         stroka += 1
#                    # spisok[j][num] = ''
#                    # k = 0
# Задача N
# N = int(input())
# M = int(input())
# row = 1
# k = 0
# data, s = [], []
# for i in range(1, M * N + 1):
#     s.append(i)
#     k += 1
#     if k == M:
#         data.append(s)
#         row += 1
#         s = []
#         k = 0
# data.append(s)
# for s in data:
#     for i in range(len(data)):
#         if k == M and i % 2 == 0:
#             print(' '.join(map(str, s)))
#         elif k == M and i % 2 != 0:
#             print(' '.join(map(str, s[::-1])))

# Задача S
# N = int(input())
# k = 0
# s = ''
# for row in range(0, N):
#     for col in range(0, N):
#         number = min(row + 1, col + 1, N - row, N - col)
#         s = f'{number} '
#         k += 1
#         if k == N:
#             print(s)
#             row += 1
#             s = ''
#             k = 0
# print(s)

# Задача T
# вторую часть кода подглядела
# number = int(input())
# best_value = 0
# best_base = 0
# for i in range(2, 11):
#     total = 0
#     while number:
#         total += number % i
#         number //= i
#     if total >= best_value and i < best_base:
#         best_value = total
#         best_base = i
# print(best_base)

# Задача D
# spisok = []
# spisok_new = []
# while True:
#     stroka = input()
#     if stroka == 'vce':
#         break
#     spisok.append(stroka)
# for k in range(len(spisok)):
#     spisok[k] = list(spisok[k])
#     for i in range(len(spisok[k])):
#         el = '#'
#         spisok = list(filter(lambda x: x != el, spisok[k]))
#         # print(new_s)
#         # sp = spisok_new.append(new_s)
#         # print(sp)
#         break
#     for j in range(0, len(spisok[k]) - len('@@@')):
#         if spisok[k][j + len('@@@'):j, -1] == '@@@':
#                 del spisok[k]
#                 for st in (spisok):
#                     print(''.join(map(str, st)))


# Задача F
# N = int(input())
# spisok = []
# spisok_z = []
# for _ in range(N):
#     stroka = input()
#     spisok.append(stroka)
# z = 'зайка'
# for stroka in spisok:
#     word = stroka.split()
#     for el in word:
#         if el == z:
#             spisok_z.append(el)
# print(len(spisok_z))

# Задача G
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a + b)

# Задача H
# N = int(input())
# spisok = []
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# z = 'зайка'
# for stroka in spisok:
#     words = stroka.split()
#     if z in words:
#         result = ' '.join(words)
#         for i, el in enumerate(words, 1):
#             index = result.index(z)
#             # index = result.index(z)
#             print(index)
#             break
#     else:
#         print('Заек нет =(')

# Задача I
# spisok = []
# while True:
#     s = input()
#     if s == 'vce':
#         break
#     spisok.append(s)
# for sp in spisok:
#     podspisok = list(map(lambda x: [x], sp))
#     for el in podspisok:
#         for i in range(1, len(el)):
#             if el[i] == '#':
#                 el.pop([i])
#         if el[0] != '#':
#             print(''.join(map(str, el)))

# spisok = []
# spisok_new = []
# while True:
#     stroka = input()
#     if stroka == '':
#         break
#     spisok.append(stroka)
# for k in range(len(spisok)):
#     el = '#'
#     spisok = list(filter(lambda x: x != el, spisok[k]))
#
#     for j in range(0, len(spisok[k]) - len('@@@')):
#             if spisok[k][j + len('@@@'):j, -1] == '@@@':
#                 del spisok[k]
#                 for st in (spisok):
#                     print(''.join(map(str, st)))

# Задача J
# spisok = []
# letters = []
# counts = [0] * len(letters)
# while True:
#     stroka = input()
#     if stroka == 'ФИНИШ':
#         break
#     spisok.append(stroka)
# for s in spisok:
#     s = s.lower()
#     letters = list(map(str, s))
# for letter in letters:
#         if (index := letters.index(letter)) != -1:
#             counts[index] += 1
#         else:
#             letters.append(letter)
#             counts.append(1)
#         if counts[index] == max(counts) and index == letters.index(letter):

# Задача L
# ka = ['манная', 'гречневая', 'пшённая', 'овсяная', 'рисовая']
# N = int(input())
# for day in range(N):
#     today = ka[day % len(ka)]
#     print(today)

# Задача M
# spisok = []
# N= int(input())
# for _ in range(N):
#     a = int(input())
#     spisok.append(a)
# b = int(input())
# for el in spisok:
#     el = el ** b
#     print(el)

# Задача N
# spisok = []
# numbers = input().split()
# b = int(input())
# numbers = [int(number) for number in numbers]
# for el in numbers:
#     el = el ** b
#     spisok.append(el)
# print(' '.join(map(str, spisok)))

# Задача O
# import math
# a = input().split()
# spisok = []
# for el in a:
#     el = int(el)
#     spisok.append(el)
# nod_0 = math.gcd(int(spisok[0]), int(spisok[1]))
# for i in range(len(spisok)):
#     nod = math.gcd(nod_0, spisok[i])
# print(nod)

# Задача Q
# s = input().split()
# for i in range(len(s)):
#     s[i] = s[i].lower()
# for word in s:
#     if word == '':
#         s = s.replace(' ', word)
# result = ''.join(map(str, s))
# if result == result[::-1]:
#     print('YES')
# else:
#     print('NO')

# Задача R
# text = input()
# reference = text[0]
# counter = 1
# text = text[1:] + '_'
# for digit in text:
#     if digit == reference:
#         counter += 1
#         print(digit, counter)
#         #break
#     else:
#         reference = digit
#         counter = 1
#         print(digit, counter)
#         #break
# #print(digit, counter)

# Задача D
# N_man = int(input())
# M_ovs = int(input())
# spisok_man = []
# spisok_ovs = []
# for _ in range(N_man):
#     s_man = input()
#     spisok_man.append(s_man)
# spisok_man = set(spisok_man)
# for _ in range(M_ovs):
#     s_ovs = input()
#     spisok_ovs.append(s_ovs)
# spisok_ovs = set(spisok_ovs)
# S = spisok_man.intersection(spisok_ovs)
# if S != set():
#     print(len(S))
# else:
#     print('Таких нет')

# Задача E
# N_man = int(input())
# M_ovs = int(input())
# spisok_man = []
# spisok_ovs = []
# for _ in range(N_man):
#     s_man = input()
#     spisok_man.append(s_man)
# spisok_man = set(spisok_man)
# for _ in range(M_ovs):
#     s_ovs = input()
#     spisok_ovs.append(s_ovs)
# spisok_ovs = set(spisok_ovs)
# S = spisok_man.symmetric_difference(spisok_ovs)
# if S != set():
#     print(len(S))
# else:
#     print('Таких нет')

# Задача F
# N_man = int(input())
# M_ovs = int(input())
# spisok_man = []
# spisok_ovs = []
# for _ in range(N_man):
#     s_man = input()
#     spisok_man.append(s_man)
# spisok_man = set(spisok_man)
# for _ in range(M_ovs):
#     s_ovs = input()
#     spisok_ovs.append(s_ovs)
# spisok_ovs = set(spisok_ovs)
# S = spisok_man.symmetric_difference(spisok_ovs)
# S = list(S)
# if S != []:
#     sorted_S = sorted(S)
#     for el in sorted_S:
#         print(el)
# if S == []:
#     print('Таких нет')

# Задача G
# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
# s = input()
# s = s.upper()
# s = s.split()
# for i in range(len(s)):
#     for el in s[i]:
#         for key, value in MORSE.items():
#             if el == key:
#                 el = value
#                 print(el)

# Задача H
# N = int(input())
# spisok_value = []
# spisok_keys = []
# for _ in range(N):
#     s = input().split()
#     spisok_keys.append(s[0])
#     spisok_value.append(s[1])
# d = dict(zip(spisok_keys, spisok_value))
# ka = input()
# for keys, value in d.items():
#     if ka == value:
#         print(keys)
#     else:
#         print('Таких нет')

# Задача I
# spisok = []
# counter = {}
# while True:
#     s = input()
#     if s == 'vce':
#         break
#     s = s.split()
#     spisok.append(s)
# for stroka in spisok:
#     for word in stroka:
#         if word in counter:
#             counter[word] += 1
#         else:
#             counter[word] = 1
# for description, count in counter.items():
#     print(description, count)

# Задача J
# translit_dict_full = {
#     # Заглавные
#     'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
#     'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
#     'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
#     'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
#     'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia',
#
#     # Строчные
#     'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
#     'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
#     'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
#     'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
#     'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
# }
# s = input()
# spisok = []
# for el in s:
#     for keys, value in translit_dict_full.items():
#         if el == keys:
#             el = value
#     spisok.append(el)
# new_spisok = list(filter(lambda x: x != 'ь' and x != 'ъ', spisok))
# print(''.join(map(str, new_spisok)))

# Задача K
# N = int(input())
# spisok = []
# # count = 0
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for i in range(len(spisok)):
# # for i in range(len(spisok) - 1):
#     count = 0
#     for j in range(len(spisok)):
#     # for j in range(i + 1, len(spisok)):
#         if spisok[i] == spisok[j]:
#             count += 1
# print(count)

# # Задача L
# N = int(input())
# spisok = []
# counter = {}
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for stroka in spisok:
#     if stroka in counter:
#         counter[stroka] += 1
#     else:
#         counter[stroka] = 1
# for description, count in counter.items():
#     print('{} - {}'.format(description, count))


# Задача M
# N = int(input())
# spisok = []
# for _ in range(N):
#     b = input()
#     spisok.append(b)
# M = int(input())
# for _ in range(M):
#     A = int(input())
#     for _ in range(A):
#         b1 = input()
#     B = int(input())
#     for _ in range(B):
#         b2 = input()

# Задача O
# s = input()
# s = s.split()
# new_spisok = []
# spisok_dict = []
# for el in s:
#     el = int(el)
#     new_el = f'{el:b}'
#     new_spisok.append(new_el)
# for element in new_spisok:
#     keys = ["digits", "units", "zeros"]
#     values = [len(element), element.count('1'), element.count('0')]
#     d = dict(zip(keys, values))
#     spisok_dict.append(d)
# print(spisok_dict)

# Задача P
# S = set()
# spisok = []
# spisok_slov = []
# while True:
#     s = input()
#     if s == 'все':
#         break
#     s = s.split()
#     spisok.append(s)
# for i in range(len(spisok)):
#     if spisok[i][0] == 'зайка' and spisok[i][len(spisok[i]) - 1] != 'зайка':
#         spisok_slov.append(spisok[i][1])
#         for j in range(2, len(spisok[i])):
#             if spisok[i][j] == 'зайка':
#                 spisok_slov.append(spisok[i][j + 1])
#                 spisok_slov.append(spisok[i][j - 1])
#     elif spisok[i][0] != 'зайка' and spisok[i][len(spisok[i]) - 1] == 'зайка':
#         spisok_slov.append(spisok[i][len(spisok[i]) - 2])
#         for j in range(len(spisok[i]) - 2):
#             if spisok[i][j] == 'зайка':
#                 spisok_slov.append(spisok[i][j + 1])
#                 spisok_slov.append(spisok[i][j - 1])
#     elif spisok[i][0] != 'зайка' and spisok[i][len(spisok[i]) - 1] != 'зайка':
#         for j in range(len(spisok[i]) - 1):
#             if spisok[i][j] == 'зайка':
#                 spisok_slov.append(spisok[i][j + 1])
#                 spisok_slov.append(spisok[i][j - 1])
#     # else:
#     elif spisok[i][0] == 'зайка' and spisok[i][len(spisok) - 1] == 'зайка':
#         spisok_slov.append(spisok[i][1])
#         spisok_slov.append(spisok[i][len(spisok[i]) - 2])
#         for  j in range(2, len(spisok[i]) - 2):
#             if spisok[i][j] == 'зайка':
#                 spisok_slov.append(spisok[i][j + 1])
#                 spisok_slov.append(spisok[i][j - 1])
# for sp in spisok_slov:
#         S.add(sp)
# for el in S:
#     print(el)

# Задача Q
# spisok = []
# spisok_fam = []
# while True:
#     s = input()
#     if s == 'все':
#         break
#     s = s.split()
#     spisok.append(s)
# for i in range(len(spisok)):
#     spisok_fam += spisok[i]
#     for j in range(len(spisok) - 1):
#             spisok_dr = []
#             if spisok[i][0] == spisok[j][0] and :
#                 spisok_dr.append(spisok[j][0])
#             elif spisok[i][k] == spisok[j][1]:
#                 spisok_dr.append(spisok[j][1])
#             d = dict(zip(list(set(spisok_fam)), spisok_dr))
#             print(d)
# # print(list(set(spisok_fam)))
# if
#
# #

# N = int(input())
# M = int(input())
# row = 1
# k = 0
# data = []
# s = ''
# for i in range(1, M * N + 1):
#     s += f'{i} ' #'{} '.format(str(i).rjust(len(s)))
#     k += 1
#     if k == M:
#         data.append(s)
#         row += 1
#         s = ''
#         k = 0
# data.append(s)
# for i in range(len(data)):
#     if i % 2 == 0:
#         print(data[i])
#     else:
#         print(data[i][::-1])

# # вторую часть кода подглядела
# number = int(input())
# best_value = 0
# best_base = 11
# spisok = []
# for i in range(2, 11):
#     total = 0
#     while number > 0:
#         total += number % i
#         number //= i
#     spisok.append(total)
#     if total == max(spisok):
#         best_value = total
#         best_base = i
# print(best_base)
#
# N = int(input())
# z = 'зайка'
# for _ in range(N):
#     s = input()
#     st = '' + s
#     if z in st:
#         index = st.index(z)
#         print(index)
#     else:
#         print('Заек нет =(')


#
# spisok = []
# stroki = []
# letters = []
# S = []
# value, l = 0, 'a'
# while True:
#     stroka = input()
#     if stroka == 'ФИНИШ':
#         break
#     stroka = stroka.lower()
#     spisok.append(stroka)
# stroki = list(map(str, spisok))
# for st in stroki:
#     for el in st:
#          letters.append(el)
# counts = [0] * (len(letters))
# for letter in letters:
#     if (index := letters.index(letter)) != -1:
#        # print(letters.index(letter))
#         counts[index] += 1
#     else:
#         letters.append(letter)
#         counts.append(1)
#     #for i in range(len(letters)):
#     # if counts[index] == max(counts) and index == letters.index(letter):
#     #         S.append(letter)
#     for i in range(len(letters)):
#         #while i == letters.index(letter):
#             if counts[i] >= value:
#                 value = counts[i]
#                 l = letter
#                 S.append(l)
#
# print(S)
# S = set(S)
# result = list(S)
# print(result)
# for element in S:
#     print(element)
# #print(value, l)
#     if counts[index] == max(counts):
#         print(counts[index])
#         print(letter)
#         S.append(letter)
# print(S)
#         #break
# #if len(S) >= 1:
# res = sorted(S)
# for element in res:
#     print(res)
    # for element in S:
    #     print(element)
#     #break
# L = int(input())
# N = int(input())
# spisok = []
# spisok_predl = [''] * L
# summa = 0
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for i in range(len(spisok)):
#     summa += len(spisok[i])
#     if summa <= len(spisok_predl):
#         spisok_predl.append(spisok[i])
#     else:
#         while True:
#             spisok_predl.append(spisok[i])
#             for j in range(len(spisok[i])):
#                 if len(spisok[i]) > 3 and j == len(spisok_predl):
#                     spisok[i] = spisok[i][:j] + '...' * (len(spisok[i]) - len(spisok[i][:j]))
#                     break
                # ...







# text = input()
# reference = text[0]
# counter = 0
# spisok = []
# # text = text[1:] + '_'
# for digit in text:
#     if digit == reference:
#         counter += 1
#         print(digit, counter)
#     else:
#         reference = digit
#         counter = 1
#         print(digit, counter)
 # for el in spisok:
 #     print(' '.join(map(str, el)))



# spisok = []
# key = []
# value = []
# N = int(input())
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for el in spisok:
#     el = el.split()
#     #key.append(el[0].replace(':', ''))
#     value.append(el[1:]) # заполняем списками
# #print(value)
# value[0] = set(value[0])
# for i in range(1, len(value)):
#         se = set(value[i]).symmetric_difference(set(value[0]))
#         print(se)


# for i in range(len(value)):
#     for element in value[i]:
#         S.append(element)
# print(S)
# # S = list(S)
# # print(sorted(S))
# for e in sorted(list(S)):
#      print(e)


# N = int(input())
# spisok = []
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for i in range(len(spisok) - 1):
#     count = 0
#     for j in range(i + 1, len(spisok)):
#         if i == j:
#             continue
#         if i != j and spisok[i] == spisok[j]:
#             count += 1
#             i += 1
#
# print(count)

# spisok = []
# count = 0
# N = int(input())
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for i in range(len(spisok)):
#     for j in range(len(spisok)):
#         if i == j:
#             continue
#         if spisok[i][0][0:len(spisok[i][0])] == spisok[j][0][0:len(spisok[j][0])] and spisok[i][2][0:len(spisok[i][0])] == spisok[j][2][0:len(spisok[j][0])]:
#             count += 1
# print(count)

# spisok = []
# spisok1 = []
# spisok2 = []
# Spisok = []
# S = ()
# while True:
#     s = input()
#     if s == '':
#         break
#     spisok.append(s)
# for stroka in spisok:
#     stroka = stroka.split()
#     Spisok.append((stroka[0], stroka[1]))
# T = sum(Spisok, ())
# for el in set(T):
#     spisok1.append(el)
# for element in sorted(spisok1):


# spisok = []
# Spisok = []
# count = 0
# N = int(input())
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for i in range(len(spisok)):
#     for j in range(len(spisok)):
#         if i == j:
#             continue
#         if spisok[i][0][0:len(spisok[i][0])] == spisok[j][0][0:len(spisok[j][0])] and spisok[i][2][0:len(spisok[i][2])] == spisok[j][2][0:len(spisok[j][2])]:
#             Spisok.append((spisok[i], spisok[j]))
# unique_pairs = list({frozenset(pair) for pair in Spisok})
# unique_pairs = [tuple(pair) for pair in unique_pairs]
#
# print(unique_pairs)
# print(len(unique_pairs))

# идею подглядела

#     print(', '.join(f'{rank} {suit}' for rank, suit in spisok[i]))
#
#
# spisok = []
# key = []
# Spisok = []
# Sp = []
# N = int(input())
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for el in spisok:
#     value = []
#     el = el.split()
#     key.append(el[0].replace(':', ''))
#     for e in el:
#         if e != el[0]:
#             e = e.replace(',', '')
#             value.append(e)
#     Spisok.append(value)
# for i in range(len(Spisok)):
#     for j in range(len(Spisok)):
#         if i == j:
#             continue
#         result = set(Spisok[i]).symmetric_difference(set(Spisok[j]))
#         Sp.append(result)
# comb_set= set().union(* Sp)
# comb_set = list(comb_set)
# for element in sorted(comb_set):
#     print(element)


#
# spisok = []
# for i in range(2):
#     s = input()
#     spisok.append(s)
# print(spisok)
# for el in spisok:
#     numbers = [el]
#     print(numbers)

# spisok = []
# spisok_letter = []
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
# for letter in letters:
#     count_of_letter = letters.count(letter)
#     spisok_letter.append(count_of_letter)
#     if count_of_letter == max(spisok_letter):
#         print(letter)
#         break

# Задачка P (сокращение заголовков)
# L = int(input())
# N = int(input())
# spisok = []
# spisok_predl = [''] * L
# summa = 0
# for _ in range(N):
#     s = input()
#     spisok.append(s)
# for i in range(len(spisok)):
#     summa += len(spisok[i])
#     if summa <= len(spisok_predl):
#         spisok_predl.append(spisok[i])
#     else:
#         while True:
#             spisok_predl.append(spisok[i])
#             for j in range(len(spisok[i])):
#                 if len(spisok[i]) > 3 and j == len(spisok_predl):
#                     spisok[i] = spisok[i][:j - 3] + '...'
#             break
#         while True:
#             spisok_predl.append(spisok[i])
#             if len(spisok[i]) < 3 and summa == len(spisok_predl):
#                 break
#                 spisok_predl.remove(spisok[i])
#                 for j in range(len(spisok[i - 1])):
#                     spisok[i - 1] = spisok[i - 1][:j - 3] + '...'
#                 # ...

# class Player:
#
#     def __init__(self, id: int, name: str, scores: int = 0, games: [] = None):
#         self.id: int = id
#         self.name: str = name
#         self.scores: int = scores
#         if games is not None:
#             self.games = games
#         else:
#             self.games = []
#
#
#     def add_result(self, game_id, scores):
#         self.games.append(game_id)
#
# import math
#
# lst = [ [1, 2], [1, 3], [1, 4] ]
# lst_numerator = [pair[0] for pair in lst]
# lst_denominator = [pair[1] for pair in lst]
# lst_denominator_new = [math.lcm(math.lcm(lst_denominator[0], lst_denominator[1]), lst_denominator[i]) for i in range(2, len(lst_denominator))]
# lst_numerator_new = [lst_numerator[i] * (lst_denominator_new[0] // lst_denominator[i]) for i in range(len(lst_numerator))]
# if not isinstance(sum(lst_numerator_new) / lst_denominator[0], int):
#     print([sum(lst_numerator_new), lst_denominator_new[0]])
# else:
#     print(sum(lst_numerator_new) / lst_denominator[0])
# print(lst_denominator_new)
# print(lst_numerator_new)
# def numerology(date):
#     result = [int(elem) for elem in date.split('/')]
#     total = 0
#     total_lst = sum(result)
#     while len(str(total_lst)) != 1:
#         for elem in str(total_lst):
#             total += int(elem)
#         total_lst = total
#     return total_lst
# print(numerology('10/13/1964'))
# date = '10/13/1964'
# # result = [int(elem) for elem in date.split('/')]
# # total_lst = sum(result)
# # while len(str(total_lst)) != 1:
# #     total = 0
# #     for elem in str(total_lst):
# #         total += int(elem)
# #     total_lst = total
#
# categories = ["A", "B", "C", "W"]
# stocklist = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
# char_1 = [string[0] for string in stocklist]
# lst = []
# for categ in categories:
#     for string in stocklist:
#         if string[0] == categ:
#             lst.append([string[0], string.split()[1]])
#     if categ not in char_1:
#         lst.append([categ, '0'])
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if i == j:
#             continue
#         else:
#             if lst[i][0] == lst[j][0]:
#                 total = int(lst[i][1]) + int(lst[j][1])
#                 lst[i][1] = str(total)
#                 lst[j][1] = '0'
# data = {}
# for letter, value in lst:
#     if letter not in data or value > data[letter]:
#         data[letter] = value
# # result_data = [(letter, data[letter]) for letter in data]
# # result = " - ".join(f"({letter} : {value})" for letter, value in result_data)
# # print(lst)
# # print(result)
# # text = "Indivisibilities"
# # result = [(char, text.lower().count(char)) for char in text.lower()]
# # result_new = sorted(list(set(result)), key=lambda x: x[1])
# # res = [pair[1] for pair in result_new]
# # res_ = [n for n in res if n == max(res) and not all(n == max(res) for n in res)]
# # print(len(res_))
# # print(result_new)
# n = 1
# s = 'I LOVE YOU!!!'
# result = []
# lowercase = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
# uppercase = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
# ]
# for word in s.split():
#     res = []
#     for char in word:
#         if char.isalpha() and char in lowercase:
#             res.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
#         elif char.isalpha() and char in uppercase:
#             res.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
#         elif char.isdigit():
#             res.append(9 - int(char))
#         else:
#             res.append(char)
#     result.append(''.join(res))
# result_new = []
# for word in result:
#     res_new = []
#     for index, char in enumerate(word):
#         if index % 2 == 0:
#             res_new.append(char.upper())
#         else:
#             res_new.append(char.lower())
#     result_new.append(''.join(res_new[::-1]))
# print(result_new)
# print(' '.join(result_new[::-1]))
# import math
# lst = []
# students = [{'name': 'Henry, Johns', 'marks': [25, 50]}, {'name': 'Timmy, Bug', 'marks': [100, 98]}, {'name': 'George, King', 'marks': [100, 85]}, {'name': 'Finn, Wish', 'marks': [45, 90]}, {'name': 'Lucy Act', 'marks': [55, 100]}]
#
# for d in students:
#     if d['marks'][0] != 0:
#         delta = ((d['marks'][-1] - d['marks'][0]) / d['marks'][0]) * 100
#         delta = math.ceil(delta)
#     else:
#         delta = 0
#     d_new = {'name': d['name'], 'improvement': delta}
#     lst.append(d_new)
# # lst_new = sorted(lst, key=lambda x: (x['improvement'], x['name']))
# # print(lst_new)
# import math
#
# g = 2
# m = 100
# n = 110
# result = []
# lst = []
# for number in range(m, n + 1):
#     if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
#             result.append(number)
# print(result)
# for elem in result:
#     for eleM in result:
#         if abs(elem - eleM) == g:
#             lst.append(sorted([elem, eleM]))
# if lst != []:
#     print(lst[0])
# else:
# #     print(None)
# from itertools import combinations
# arr = [1,2,3,10,-5]
# n = 2
# result = list(combinations(arr, n))
# result_new = [tup for tup in result if all(arr.index(tup[i]) + 1 == arr.index(tup[i + 1]) for i in range(len(tup) - 1))]
# print(result_new)

# def is_happy(n):
#     n_new = n
#     flag = False
#     while n_new != 1:
#         total = 0
#         for elem in str(n_new):
# #             total += int(elem) ** 2
# #         n_new = total
# #         flag = True
# #     if flag:
# #         return True
# #     return False
# # print(is_happy(3))
#
# #"Better than I am him"
# sentence = "I am the best"
# result = []
# lst_sentence = sorted(sentence.split(), key=lambda x: len(x))
# lst_sentence_2 = sorted(sentence.split(), key=lambda x: len(x), reverse=True)
# lst = list(zip(lst_sentence, lst_sentence_2))
# for word in sentence.split():
#     flag = False
#     for i in range(len(lst)):
#         if lst[i][0] == word:
#             result.append(lst[i][1])
#             flag = True
#             break
#         elif lst[i][1] == word:
#             result.append(lst[i][0])
#             flag = True
#             break
#     if not flag:
#         result.append(word)
# string = ' '.join(result)
# res = []
# for word in string.split():
#     string_lst = [char.lower() if char != 'I' or word.index(char) !=0 else char for char in word]
#     res.append(''.join(string_lst))
# string_lst = ' '.join(res)
# print(string_lst[0].upper() + string_lst[1:])
# #
# # print(lst)
# # print(result)
# l, r = 10, 12
# result = []
# lst_number = []
# for number in range(l, r + 1):
#     lst_number.append(number)
#     total = 0
#     for elem in str(number):
#         total += int(elem)
#     result.append(total)
# lst = list(zip(lst_number, result))
# lst_new = [[pair[0] - pair[1], pair[0] + pair[1]] for pair in lst]
# res = list(zip(lst_number, lst_new))
# spisok = [(pair[0], list(range(pair[1][0], pair[1][1] + 1))) for pair in res]
# Result = []
# for pair in spisok:
#     for i in range(len(pair[1])):
#         if pair[0] < pair[1][i] and pair[1][i] in list(range(l, r + 1)):
#             Result.append((pair[0], pair[1][i]))
# print(len(Result))
# def split(arr):
#     arr1 = [item for lst in arr for item in lst]
#     arr2 = [[len(lst)] for lst in arr]
#     return [arr1, arr2]
# print(split([[1,3,5],[2,4,6],[7,8,9]]))
#
# def join(arr1, arr2):
#     arr = []
#     for lst in arr2:
#         arr_i = []
#         for i in range(lst[0]):
#             arr_i.append(arr1[i])
#         arr.append(arr_i)
#     return arr
# arr1=[1,2,3,4,5,6,7,8,9,10]
# arr2=[[1],[2],[3],[4]]
# print(join(arr1, arr2))

# def longest_word(letters):
#     lst_len = [len(word) for word in words]
#     result = []
#     for word in words:
#         if all(char in letters for char in word) and len(word) == max(lst_len):
#             result.append(word)
#     if len(result) == 1:
#         return [result[0]]
#     elif len(result) > 1:
#         return sorted(result)
#     return None
# s = "breakCamelCase"
# result = []
# for char in s:
#     if char.isupper():
#         result.append(s[:s.index(char)] + ' ' + s[s.index(char):])
# if result != []:
# #     print(result)
# # else:
# #     print(s)
# item_index = 5
# collection = ['a','b','c','d','e','f']
# items_per_page = 4
# # i = 0
# # lst = []
# # while i < len(collection):
# #     lst_page = []
# #     for _ in range(items_per_page):
# #         if i < len(collection):
# #             lst_page.append(collection[i])
# #             i += 1
# #         else:
# #             break
# #     lst.append(lst_page)
# # result = []
# # for i in range(len(lst)):
# #     for elem in collection:
# #         if elem in lst[i] and item_index == collection.index(elem):
# #             result.append(i)
# # print(result)
# from collections import Counter
#
# words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
# term = 'aple'
# result = []
# lst = []
# spisok = []
# for word in words:
#     common_elements = Counter(term) & Counter(word)
#     result.append(common_elements)
# lst_len = [len(res) for res in result]
# for index, word in enumerate(words):
#     if lst_len[index] == max(lst_len):
#         lst.append(word)
# if len(lst) > 1:
#     lst_res = [(lst[i], abs(len(lst[i]) - len(term))) for i in range(len(lst))]
#     res = [pair[1] for pair in lst_res]
#     for pair in lst_res:
#         if pair[1] == min(res):
#             spisok.append(pair[0])
#
# print(spisok)
# print(lst)
# print(result)
# print(lst_len)

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# index = 0
# lst = []
# for i in range(len(arr) * (len(arr) + 1) // 2):
#     result = []
#     start = 0
#     count = 0

#
#
# print(lst)


