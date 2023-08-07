# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы обоих списков;
# ■ Сформировать третий список, содержащий элементы обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное значение
# каждого из списков.

from random import randint

s1 = [randint(1,10)for x in range(5)]
s2 = [randint(1,10)for x in range(5)]
print('Первый список:', s1)
print('Второй список:', s2)

s3 = s1 + s2
print('Элементы 2х списков:', s3)

s4 = sorted(set(s3), key=s3.index)
print('Список без повторений:', s4)

s5 = [i for i in s3 if i in s1 and i in s2]
print('Общие элементы:', s5)

s6 = sorted(list(set(s1)) + list(set(s2)), key=s3.index)
print('Только уникальные элементы:', s6)

s7 = [min(s3),max(s3)]
print('минимум и максимум:', s7)


# Задание 2
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

a = [3, 4, -1, 7, -2, 5, 4, 5, -5, -3, 4, 10, -10, 9, -2]
sum = 0
pro = 1

for i in a:
    if i < 0:
        sum += i
print( 'Сумма отрицательных:', sum, sep='\n')

for i in a:
    if i % 2 == 0:
        sum += i
print('Сумма четных чисел;', sum, sep='\n')

for i in a:
    if i % 5 == 0:
        sum += i
print('Сумма не четных чисел:', sum, sep='\n')

for i in a:
    pro *= i
print(f'Максимум:{max(a)}\nМинимум:{min(a)}\nПроизведение: {pro}')

print(next(i for i in a if i > 0) * next(i for i in reversed(a) if i > 0))


# Задание 3
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
# ■ Создать список целых, содержащий только четные числа из списка;
# ■ Создать список целых, содержащий только нечетные числа из списка;
# ■ Создать список целых, содержащий только отрицательные числа из списка;
# ■ Создать список целых, содержащий только положительные числа из списка

import random
a = random.sample(range(-9,10), 10)
print(a)
b = []
c = []
d = []
e = []
for i in a:
    if i % 2 == 0:
        b += [i]
    if i % 2 != 0:
        c += [i]
    if i < 0:
        d += [i]
    if i > 0:
        e += [i]

print('Четные числа:', b)
print('Не четные числа:', c)
print('Отрицательные числа:', d)
print('Положительные числа:', e)


# 1. Дан список [-1, 0, 5, 3, 2].
# Необходимо изменить его, увеличив каждое значение на 7.2.
# 2. Пользователь вводит с клавиатуры N значений (строки или числа).
# На их основе сформировать список, состоящий из продублированных элементов.
# (Например, из значений 1, 5, "abc" формируется список [1, 1, 5, 5, "abc", "abc"]).
# 3. Пользователь вводит N значений в список.
# Необходимо проверить: было ли введено число 5.

a = [-1, 0, 5, 3, 2]
f = 0
while f <= len(a)-1:
    a[f] += int(a[f]) * 7.2
    f += 1
print(a)

a = input('Введи N значений ')
b = a.split(',')
print(b)
c = []
f = 0
while f <= len(b)-1:
    c += [b[f]]
    c += [b[f]]
    f += 1
print(c)



