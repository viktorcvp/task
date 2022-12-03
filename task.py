# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

"""
def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")


lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def mult_lst(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    print(new_lst)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)
"""
# Задача №16: Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

# n = int(input("Введите число n: "))
# s = 0
# for i in range(1, n + 1):
# s += (1 + 1 / i) ** i
# print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(s,2)}")

# Задача №17: Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
import random


def write_file(number):
    with open("file.txt", "w") as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open("file.txt", "r") as data:
        indexs = list(map(int, data.readlines()))
    return indexs


# pyt
# print("vik")
# print(f"{20 * 2}")
def greet(name):
    return "Привет, " + name


# name = "Олег"
# print(f"{greet(name)}")
# print(f"{{{{Pythonru}}}}")
# person = {"name": "Игорь", "age": 19}
# print(f"{person['name']}, {person['age']} лет.")
import cmath

# a = float(input("Input A: "))
# b = float(input("Input B: "))
# c = float(input("Input C: "))

# d = (b**2) - (4 * a * c)
# if d > 0:
#     x1 = (-b - cmath.sqrt(d)) / (2 * a)
#     x2 = (-b + cmath.sqrt(d)) / (2 * a)
#     print(x1, x2)
# elif d == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     print("Корней нет")

# 4_1. Вычислить число Пи c заданной точностью d
# import math

# d = int(input("задайте точность числа π,чисел после запятой : "))

# if d < 1 or d > 10:
#     print("точность выходит за границы диапазона")
# else:
#     p = str(math.pi)
#     print(p[0 : (d + 2)])
# 4_2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2  # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"{lst}")

# 4_3.Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# from random import randint

# N = int(input("Введите число : "))
# mass = []

# for i in range(N):
#     mass.append(randint(0, N))
# print(mass)
# mass2 = []
# for i in mass:
#     if mass.count(i) == 1:
#         mass2.append(i)
# print(mass2)

# 4_4. Задана натуральная степень k. Сформировать случайным
#  образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# from random import randint
# import itertools

# k = randint(2, 3)


# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# def get_polynomial(k, ratios):
#     var = ["*x^"] * (k - 1) + ["*x"]
#     polynomial = [
#         [a, b, c]
#         for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue="")
#         if a != 0
#     ]
#     for x in polynomial:
#         x.append(" + ")
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = " = 0"
#     return "".join(map(str, polynomial)).replace(" 1*x", " x")


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open("33_Polynomial.txt", "w") as data:
#     data.write(polynom1)
def sumEql():
    with open("file 44(1).txt", "r") as data:
        eql1 = data.readline()

    with open("file 44(2).txt", "r") as data:
        eql2 = data.readline()

    print(eql1 + eql2)


sumEql()
