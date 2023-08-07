# Задание 1
# Напишите функцию, которая отображает пустой или заполненный квадрат
# из некоторого символа. Функция принимает в качестве параметров:
# длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой

# def func(s, n, e):
#     line = n * s
#     if e:
#         for i in range(n):
#             print(line)
#     else:
#         print(line)
#         for i in range(n - 2):
#             print(s + " " * (n - 2) + s)
#         print(line)
#
#
# func("t", 5, False)


# Задание 2
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров.
# Если границы диапазона перепутаны
# (например, 5 — верхняя граница, 25 — нижняя граница), их нужно поменять местами.


# def fan(x, y):
#     if x > y:
#         x, y = y, x
#     p=1
#     for i in range(x + 1, y):
#         p*=i
#         print(p)
# fan(int(input("x =: ")),int(input("y =: ")))


# Задание 3
# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра. Из функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.


# def fun(a):
#     print(len(str(a)))
#
# fun(int(input('Введите число: ')))


# Задание 4
# Напишите функцию, которая проверяет является ли число палиндромом.
# Число передаётся в качестве параметра. Если число палиндром нужно
# вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй
# перевернутой части цифр. Например, 123321 — палиндром
# (первая часть 123, вторая 321, которая после переворота становится 123),
# 546645 — палиндром, а 421987 — не палиндром.


# def fun(x):
#     line = str(x)
#     b = len(line)
#     if b % 2 == 0:
#        s = line[:b//2]
#        s1 = line[b//2:]
#        if s == s1[::-1]:
#            print('Полиндром')
#        else:
#            print('Не полиндром')
#     else:
#         print('Не полиндром')
#
# fun(input('Введите:'))



# Задание 5
# Напишите функцию, которая отображает горизонтальную или вертикальную
# линию из некоторого символа. Функция принимает в качестве параметра:
# длину линии, направление, символ.

# def fun(a, b, c):
#     if b == 'горизонтальное':
#         print(a * c)
#     elif b == 'вертикальное':
#         for i in range(a):
#             print(c)
#
# fun(5, 'горизонтальное', '.')


